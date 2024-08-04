from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import CreationForm, DenialReasonForm
from .models import Requests
def create_request(request):
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            existing_requests = Requests.objects.filter(title__iexact=title)
            if existing_requests.exists():
                form.add_error(None, 'A request with this title already exists.]')
            else:
                requests = form.save(commit=False)
                requests.created_by = request.user
                requests.save()
                return redirect('repair_requests:request_list')
        else: 
            return render(request,'repair_requests/create_request.html', {'form': form})
    else:
        return render(request,'repair_requests/create_request.html', {'form': CreationForm})        

def my_requests(request):
    requests = Requests.objects.filter(created_by=request.user)
    context = {'requests': requests}
    return render(request, 'repair_requests/my_requests.html', context)

def delete_request(request, requests_id):
    requests = get_object_or_404(Requests, pk=requests_id) 

    if request.method == 'POST': 
        requests.delete() 
        return redirect('requests:requestn_list')  
    else:
        context = {'requests': requests}
        return render(request, 'requests/delete_confirmation.html', context)
    
def deny_request(request,requests_id):
    requests = get_object_or_404(Requests, pk=requests_id)
    denial_reason_form = DenialReasonForm(request.POST)

    if request.method == 'POST':
        
        if denial_reason_form.is_valid():
            denial_reason = denial_reason_form.cleaned_data['denial_reason']
            requests.denial_reason = denial_reason
            requests.is_denied = True
            requests.is_moderated = True
            requests.save()
            return redirect('repair_requests:request_list')
        else:
            return HttpResponse('suck')


    context = {'requests': requests, 'denial_reason_form': denial_reason_form}
    return render(request, 'repair_requests/requests_deny.html', context)

def request_list(request):
    requests = Requests.objects.filter(is_moderated=True,is_denied = False)
    context = {'requests': requests}
    return render(request, 'repair_requests/requests_list.html', context)

def unmoderated_request_list(request):
    unmoderated_requests = Requests.objects.filter(is_moderated=False)
    denied_requests = Requests.objects.filter(is_denied=True)
    context = {
        'requests': unmoderated_requests,
        'denied_requests': denied_requests,
        }
    return render(request, 'repair_requests/unmoderated_request_list.html', context)

def moderate_request(request, requests_id):
    if request.method == 'POST':
        try:
            requests = Requests.objects.get(pk=requests_id)
            requests.is_moderated = True
            requests.is_denied = False
            requests.save()
            return redirect('repair_requests:request_list')
        except requests.DoesNotExist:
            message = "Suggestion not found."
            return redirect('repair_requests:request_list')

    else:  
        return render(request, 'repair_requests/moderate_request.html')
    
def request_detail(request, requests_id):
    requests =Requests.objects.get(pk=requests_id)
    context = {
        'requests': requests,
        'moderators': ['Модератор предложений','Школьная администрация','Системный администратор'],
        'technician': ['Технический персонал','Школьная администрация','Системный администратор','Заведующий хозяйством'],
        }
    return render(request, 'repair_requests/requests_detail.html', context)

def mark_complete(request, requests_id):
    requests = Requests.objects.get(pk=requests_id)
    if request.method == 'POST':
        requests.is_complete = True
        requests.completed_by = request.user
        requests.completed_on = timezone.now()
        requests.save()
        return redirect('repair_requests:request_list')