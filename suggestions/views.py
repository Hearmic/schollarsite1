from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from .models import Suggestion
from .forms import SuggestionForm, DenialReasonForm  


@login_required
def create_suggestion(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.user = request.user
            suggestion.save()
            return redirect('suggestions:suggestion_list')
        else:
            # Handle form validation errors 
            pass
    else:
        form = SuggestionForm()
    context = {'form': form}
    return render(request, 'suggestions/create_suggestion.html', context)

@login_required
def my_suggestions(request):
    suggestions = Suggestion.objects.filter(user=request.user)
    context = {'suggestions': suggestions}
    return render(request, 'suggestions/my_suggestions.html', context)

@login_required
def delete_suggestion(request, suggestion_id):
    suggestion = get_object_or_404(Suggestion, pk=suggestion_id)  # Get suggestion by ID
    suggestion.delete()  # Delete the suggestion
    return redirect('suggestions:suggestion_list')  # Redirect to suggestions list view (replace with your URL name)
    
@login_required
def deny_suggestion(request, suggestion_id):
    suggestion = get_object_or_404(Suggestion, pk=suggestion_id)
    denial_reason_form = DenialReasonForm(request.POST)
    if request.method == 'POST':
        if denial_reason_form.is_valid():
            denial_reason = denial_reason_form.cleaned_data['denial_reason']
            suggestion.denial_reason = denial_reason
            suggestion.is_denied = True
            suggestion.is_moderated = True
            suggestion.save()
            return redirect('suggestions:suggestion_list')
        else:
            return HttpResponse('suck')
        # ... other checks (e.g., not authenticated or not a moderator) ...

    context = {'suggestion': suggestion, 'denial_reason_form': denial_reason_form}
    return render(request, 'suggestions/suggestion_deny.html', context)

@login_required
def suggestion_list(request):
    suggestions = Suggestion.objects.filter(is_moderated=True,is_denied = False).order_by('-votes_for')
    context = {
        'suggestions': suggestions,
        'moderators': ['Модератор предложений','Школьная администрация','Системный администратор']
        }
    return render(request, 'suggestions/suggestions_list.html', context)

@login_required
def suggestion_detail(request, suggestion_id):
    suggestion =Suggestion.objects.get(pk=suggestion_id)
    context = {
        'suggestion': suggestion,
        'moderators': ['Модератор предложений','Школьная администрация','Системный администратор']
        }
    return render(request, 'suggestions/suggestion_detail.html', context)

@login_required
def vote_for(request, suggestion_id):
    suggestion = get_object_or_404(Suggestion, pk=suggestion_id)

    if request.method == 'POST':
        if request.user not in suggestion.voters_for.all():
            suggestion.voters_for.add(request.user)
            suggestion.votes_for += 1
            suggestion.save()
        context = {'suggestion': suggestion }
        return render(request, 'suggestions/suggestion_detail.html', context)

    context = {'suggestion': suggestion}
    return render(request, 'suggestions/suggestion_detail.html', context)

@login_required
def vote_against(request, suggestion_id):
    suggestion = get_object_or_404(Suggestion, pk=suggestion_id)
    if request.method == 'POST':
        if request.user not in suggestion.voters_against.all():
            suggestion.voters_against.add(request.user)
            suggestion.votes_against += 1
            suggestion.save()
        context = {'suggestion': suggestion}
        return render(request, 'suggestions/suggestion_detail.html', context)

    context = {'suggestion': suggestion}
    return render(request, 'suggestions/suggestion_detail.html', context)

@login_required
def unmoderated_suggestion_list(request):
    unmoderated_suggestions = Suggestion.objects.filter(is_moderated=False)
    denied_suggestions = Suggestion.objects.filter(is_denied=True)
    context = {
        'suggestions': unmoderated_suggestions,
        'denied_suggestions': denied_suggestions,
        }
    return render(request, 'suggestions/unmoderated_suggestion_list.html', context)

@login_required
def moderate_suggestion(request, suggestion_id):
    suggestion = Suggestion.objects.get(pk=suggestion_id)
    suggestion.is_moderated = True
    suggestion.is_denied = False
    suggestion.save()
    return redirect('suggestions:suggestion_list')

