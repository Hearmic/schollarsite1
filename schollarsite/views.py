from django.shortcuts import redirect


def redirect_to_login(request):
    if request.user.is_authenticated is True:
        return redirect('main:home')
    else:
        return redirect('users:login')
