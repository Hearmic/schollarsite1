from django.shortcuts import render
from schedules.models import school_schedule
# Create your views here.
def main(request):
    schedules = school_schedule.objects.all()  # Fetch all schedules
    context = {
        'schedules': schedules
    }
    return render(request, 'schedules/display.html', context)