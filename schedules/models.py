from django.db import models
from users.models import User

class Lessons(models.Model):
    name = models.CharField(max_length=20)
    teacher = models.ForeignKey(User, related_name='lesson_teacher')
    classroom = models.CharField(max_length=20)
    def __str__(self):
        return self.name + '' + self.teacher
    
class school_schedule (models.Model):
    grade = models.IntegerField()
    lilera = models.CharField(max_length=1)
    # Понедельник
    monday_lesson1 = models.ForeignKey(Lessons, related_name='monday_lesson1',null=True, blank=True)
    monday_lesson2 = models.ForeignKey(Lessons, related_name='monday_lesson2',null=True, blank=True)
    monday_lesson3 = models.ForeignKey(Lessons, related_name='monday_lesson3',null=True, blank=True)
    monday_lesson4 = models.ForeignKey(Lessons, related_name='monday_lesson4',null=True, blank=True)
    monday_lesson5 = models.ForeignKey(Lessons, related_name='monday_lesson5',null=True, blank=True)
    monday_lesson6 = models.ForeignKey(Lessons, related_name='monday_lesson6',null=True, blank=True)
    monday_lesson7 = models.ForeignKey(Lessons, related_name='monday_lesson7',null=True, blank=True)
    monday_lesson8 = models.ForeignKey(Lessons, related_name='monday_lesson8',null=True, blank=True)
    monday_lesson9 = models.ForeignKey(Lessons, related_name='monday_lesson9',null=True, blank=True)
    # Вторник
    tuesday_lesson1 = models.ForeignKey(Lessons, related_name='tuesday_lesson1',null=True, blank=True)
    tuesday_lesson2 = models.ForeignKey(Lessons, related_name='tuesday_lesson2',null=True, blank=True)
    tuesday_lesson3 = models.ForeignKey(Lessons, related_name='tuesday_lesson3',null=True, blank=True)
    tuesday_lesson4 = models.ForeignKey(Lessons, related_name='tuesday_lesson4',null=True, blank=True)
    tuesday_lesson5 = models.ForeignKey(Lessons, related_name='tuesday_lesson5',null=True, blank=True)
    tuesday_lesson6 = models.ForeignKey(Lessons, related_name='tuesday_lesson6',null=True, blank=True)
    tuesday_lesson7 = models.ForeignKey(Lessons, related_name='tuesday_lesson7',null=True, blank=True)
    tuesday_lesson8= models.ForeignKey(Lessons, related_name='tuesday_lesson8',null=True, blank=True)
    tuesday_lesson9 = models.ForeignKey(Lessons, related_name='tuesday_lesson9',null=True, blank=True)
    #Среда
    wednesday_lesson1 = models.ForeignKey(Lessons, related_name='wednesday_lesson1',null=True, blank=True)
    wednesday_lesson2 = models.ForeignKey(Lessons, related_name='wednesday_lesson2',null=True, blank=True)
    wednesday_lesson3 = models.ForeignKey(Lessons, related_name='wednesday_lesson3',null=True, blank=True)
    wednesday_lesson4 = models.ForeignKey(Lessons, related_name='wednesday_lesson4',null=True, blank=True)
    wednesday_lesson5 = models.ForeignKey(Lessons, related_name='wednesday_lesson5',null=True, blank=True)
    wednesday_lesson6 = models.ForeignKey(Lessons, related_name='wednesday_lesson6',null=True, blank=True)
    wednesday_lesson7 = models.ForeignKey(Lessons, related_name='wednesday_lesson7',null=True, blank=True)
    wednesday_lesson8 = models.ForeignKey(Lessons, related_name='wednesday_lesson8',null=True, blank=True)
    wednesday_lesson9 = models.ForeignKey(Lessons, related_name='wednesday_lesson9',null=True, blank=True)
    #Четверг
    thursday_lesson1 = models.ForeignKey(Lessons, related_name='thursday_lesson1',null=True, blank=True)
    thursday_lesson2 = models.ForeignKey(Lessons, related_name='thursday_lesson2',null=True, blank=True)
    thursday_lesson3 = models.ForeignKey(Lessons, related_name='thursday_lesson3',null=True, blank=True)
    thursday_lesson4 = models.ForeignKey(Lessons, related_name='thursday_lesson4',null=True, blank=True)
    thursday_lesson5 = models.ForeignKey(Lessons, related_name='thursday_lesson5',null=True, blank=True)
    thursday_lesson6 = models.ForeignKey(Lessons, related_name='thursday_lesson6',null=True, blank=True)
    thursday_lesson7 = models.ForeignKey(Lessons, related_name='thursday_lesson7',null=True, blank=True)
    thursday_lesson8 = models.ForeignKey(Lessons, related_name='thursday_lesson8',null=True, blank=True)
    thursday_lesson9 = models.ForeignKey(Lessons, related_name='thursday_lesson9',null=True, blank=True)
    #Пятница
    friday_lesson1 = models.ForeignKey(Lessons, related_name='friday_lesson1',null=True, blank=True)
    friday_lesson2 = models.ForeignKey(Lessons, related_name='friday_lesson2',null=True, blank=True)
    friday_lesson3 = models.ForeignKey(Lessons, related_name='friday_lesson3',null=True, blank=True)
    friday_lesson4 = models.ForeignKey(Lessons, related_name='friday_lesson4',null=True, blank=True)
    friday_lesson5 = models.ForeignKey(Lessons, related_name='friday_lesson5',null=True, blank=True)
    friday_lesson6 = models.ForeignKey(Lessons, related_name='friday_lesson6',null=True, blank=True)
    friday_lesson7 = models.ForeignKey(Lessons, related_name='friday_lesson7',null=True, blank=True)
    friday_lesson8 = models.ForeignKey(Lessons, related_name='friday_lesson8',null=True, blank=True)
    friday_lesson9 = models.ForeignKey(Lessons, related_name='friday_lesson9',null=True, blank=True)
    #Суббота
    saturday_lesson1 = models.ForeignKey(Lessons, related_name='saturday_lesson1',null=True, blank=True)
    saturday_lesson2 = models.ForeignKey(Lessons, related_name='saturday_lesson2',null=True, blank=True)
    saturday_lesson3 = models.ForeignKey(Lessons, related_name='saturday_lesson3',null=True, blank=True)
    saturday_lesson4 = models.ForeignKey(Lessons, related_name='saturday_lesson4',null=True, blank=True)
    saturday_lesson5 = models.ForeignKey(Lessons, related_name='saturday_lesson5',null=True, blank=True)
    saturday_lesson6 = models.ForeignKey(Lessons, related_name='saturday_lesson6',null=True, blank=True)
    saturday_lesson7 = models.ForeignKey(Lessons, related_name='saturday_lesson7',null=True, blank=True)
    saturday_lesson8 = models.ForeignKey(Lessons, related_name='saturday_lesson8',null=True, blank=True)
    saturday_lesson9 = models.ForeignKey(Lessons, related_name='saturday_lesson9',null=True, blank=True)
    #Воскресенье
    sunday_lesson1 = models.ForeignKey(Lessons, related_name='sunday_lesson1',null=True, blank=True)
    sunday_lesson2 = models.ForeignKey(Lessons, related_name='sunday_lesson2',null=True, blank=True)
    sunday_lesson3 = models.ForeignKey(Lessons, related_name='sunday_lesson3',null=True, blank=True)
    sunday_lesson4 = models.ForeignKey(Lessons, related_name='sunday_lesson4',null=True, blank=True)
    sunday_lesson5 = models.ForeignKey(Lessons, related_name='sunday_lesson5',null=True, blank=True)
    sunday_lesson6 = models.ForeignKey(Lessons, related_name='sunday_lesson6',null=True, blank=True)
    sunday_lesson7 = models.ForeignKey(Lessons, related_name='sunday_lesson7',null=True, blank=True)
    sunday_lesson8 = models.ForeignKey(Lessons, related_name='sunday_lesson8',null=True, blank=True)
    sunday_lesson9 = models.ForeignKey(Lessons, related_name='sunday_lesson9',null=True, blank=True)

class event(models.Model):
    starts_on = models.DateField()
    ends_on = models.DateField(blank=True,null=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    picture = models.ImageField()

class club_lesson(models.Model):
    name = models.CharField()
    club = models.CharField()
    teacher = models.ForeignKey(User, related_name='club_teacher',null=True, blank=True)
    classrom = models.CharField(max_length=20)
    day = models.CharField(max_length=20)
    lesson = models.IntegerField()
