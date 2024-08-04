from django.contrib.auth.middleware import AuthenticationMiddleware
from django.shortcuts import redirect

class UserRedirectMiddleware(AuthenticationMiddleware):
    def process_request(self, request):
        if request.user.is_authenticated: # если пользователь авторизован, перенаправляем его на главную сраницу
            return redirect('/main/') 
        else:
            return redirect('/users/login/') # если нет перенаправляем на страницу авторизации
