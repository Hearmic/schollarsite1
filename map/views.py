from django.shortcuts import render

from django.shortcuts import render

def map(request):
    context={
        '1': True
    }
    return render(request,'map/map.html',context )
