from rest_framework import serializers
from .models import calendar_data

class calendar_data_serializer(serializers.ModelSerializer):
    class Meta:
        model = calendar_data
        fields = []   #Прописать все строки модели