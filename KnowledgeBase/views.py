from django.shortcuts import redirect, render, get_object_or_404

from schollarsite.decorators import allowed_user_groups
from .models import StudyMaterial, Subject, FavoriteMaterial, Answer, Question
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import AddStudyMaterialForm, QuestionForm, AnswerForm
# Далаир 11"В" и Ника Кавору были тут


@login_required
def home(request):
    subjects = Subject.objects.all()
    # Поиск материалов
    query = request.GET.get('q')
    search_results = []
    if query:
        # Если есть поисковый запрос, получаем материалы, которые содержат этот запрос в названии или описании
        search_results = StudyMaterial.objects.filter(title__icontains=query) | StudyMaterial.objects.filter(description__icontains=query)
        # TODO: готов сервер с Elasticsearch и индексация осталось прикрутить его суда
        paginator = Paginator(search_results, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        # Рекомендуемые материалы (например, материалы с наибольшим количеством просмотров)
        materials = StudyMaterial.objects.order_by('-views')
        paginator = Paginator(materials, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    # Отправка всех данных в шаблон
    context = {
        'page': page_obj,
        'subjects': subjects
    }

    return render(request, 'knowledge_base/home.html', context)


@login_required
def material_detail(request, pk):

    material = get_object_or_404(StudyMaterial, pk=pk)
    files = material.files

    material.views += 1
    material.save()

    return render(request, 'knowledge_base/material_detail.html', {'material': material, 'files': files})


# Добавление материала в избранное (доступно только авторизованным пользователям)
@login_required
def add_to_favorites(request, pk):
    material = get_object_or_404(StudyMaterial, pk=pk)

    # Проверяем, есть ли уже этот материал в избранном у пользователя
    created = FavoriteMaterial.objects.get_or_create(user=request.user, material=material)

    if created:
        message = "Материал успешно добавлен в избранное."
    else:
        message = "Этот материал уже находится в вашем избранном."  # TODO: Нужно придумать где отображать месседжы

    return render(request, 'knowledge_base/favorite_added.html', {'message': message})


@login_required
def favorite(request):
    favorite = FavoriteMaterial.objects.filter(user=request.user)
    return render(request, 'knowledge_base/favorite.html', {'favorite': favorite})


@login_required
def remove_from_favorites(request, pk):
    material = get_object_or_404(StudyMaterial, pk=pk)
    favorite = FavoriteMaterial.objects.filter(user=request.user, material=material)
    if favorite:
        favorite.delete()
        message = 'Материал был удален из избранного'
    else:
        message = 'Ошибка. Не удалось найти материал'
    return render(request, 'knowledge_base/favorite_removed.html', {'message': message})


@login_required
def subject_materials(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    material = get_object_or_404(StudyMaterial, subject=subject)
    return render(request, 'knowledge_base/subject_materials.html', {'subject': subject, 'material': material})


@login_required
def favorite_materials(request):
    favorites = FavoriteMaterial.filter(user=request.user)
    context = {
        'favorites': favorites,
    }
    return render(request, 'knowledge_base/favorite_materials.html', context)


@login_required
@allowed_user_groups(allowed_groups=['Школьная администрация', 'Системный администратор', 'Учитель'])
def add_material(request):
    form = AddStudyMaterialForm(request.POST)
    if form.is_valid():
        material = form.save(commit=False)
        material.author = request.user
        material.save()
        return redirect('knowledge_base:home')
    return render(request, 'knowledge_base/add_study_material.html')


@login_required
@allowed_user_groups(allowed_groups=['Школьная администрация', 'Системный администратор', 'Учитель'])
def edit_material(request, pk):
    material = get_object_or_404(StudyMaterial, pk=pk)
    form = AddStudyMaterialForm(request.POST or None, instance=material)
    if form.is_valid():
        material = form.save(commit=False)
        material.save()
        return redirect('knowledge_base:material_detail', pk=material.pk)
    return render(request, 'knowledge_base/edit_study_material.html', {'form': form, 'material': material})


@login_required
@allowed_user_groups(allowed_groups=['Школьная администрация', 'Системный администратор', 'Учитель'])
def statistics_page(request):
    total_materials = StudyMaterial.objects.count()
    total_subjects = Subject.objects.count()
    most_viewed_material = StudyMaterial.objects.order_by('-views').first()
    context= {
        'total_materials': total_materials,
        'total_subjects': total_subjects,
        'most_viewed_material': most_viewed_material
    }
    return render(request,'knowledge_base/statistics.html', context)


@login_required
def add_question(request, material_id):
    quiz = StudyMaterial.objects.get(id=material_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            return redirect('add_answers', question_id=question.id)
    else:
        form = QuestionForm()
    return render(request, 'quiz/add_question.html', {'form': form, 'quiz': quiz})


@login_required
def add_answers(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('add_answers', question_id=question_id)  # можно добавить несколько ответов
    else:
        form = AnswerForm()
    return render(request, 'quiz/add_answers.html', {'form': form, 'question': question})


@login_required
def take_quiz(request, material_id):
    quiz = StudyMaterial.objects.get(id=material_id)
    if request.method == 'POST':
        score = 0
        total_correct = 0
        for question in quiz.questions.all():
            selected_answer_id = request.POST.get(str(question.id))
            selected_answer = Answer.objects.get(id=selected_answer_id)
            if selected_answer.is_correct:
                score += 1
            total_correct += 1
        return render(request, 'quiz/quiz_result.html', {'score': score, 'total_correct': total_correct, 'quiz': quiz})
    return render(request, 'quiz/take_quiz.html', {'quiz': quiz})
