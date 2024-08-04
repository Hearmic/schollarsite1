from django.shortcuts import redirect
from django.contrib.auth.models import Group

def redirect_to_login(request) :
    if request.user.is_authenticated == True :
        return redirect('main:home')
    else :
        return redirect('users:login')
    


