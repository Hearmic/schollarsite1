from typing import Any
from django.http import HttpResponse #нужна доля возврата html запросов
from django.shortcuts import render


def index(request):
 context: dict[str,Any]={ # нужна для передачи данных в .html шаблон
  'title': 'Home',
  'teachers':  ['Учитель', 'Классный руководитель', 'Школьная администрация'],
 }

 return render(request, 'main/index.html', context) #возвращаем рендер .html файла в папке /templates(поиск тут по дефолту)/main/index.html; заполняем данные шаблона переменной 'context'

def teachers_list(request):
    return render(request, 'main/teachers_list.html') #возвращаем рендер .html файла в папке /templates(поиск тут по дефолту)/main/teachers_list.html;

def design_system (request):
    return render(request, 'main/design_system.html')