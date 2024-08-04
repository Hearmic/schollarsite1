from django.shortcuts import render
from typing import Any
from rest_framework.views import APIView 
from .models import calendar_data
from .serializer import calendar_data_serializer
from rest_framework.response import Response 

from calender import serializer

class calendarView(APIView):
    def get(self, request):
        output = [
            {
                "title": output.title
            }
        ]
    def post(self,request):
        serializer = calendar_data_serializer(data=request.data)
        if serializer.is_valid(raise_exeption = True):
            serializer.save()
            return Response(serializer.data)

def calender(request):
    return render(request, 'calender/calendar.html')