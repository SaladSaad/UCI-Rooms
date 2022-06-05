from django.shortcuts import render
from django.http import HttpResponse

from .models import Course

# Create your views here.
def show_graph_view(request):
    context = {"nani":'bruh', "mylist":['nothing at all','wubba lubba dub dub',120345]}
    return render(request, 'index.html', context)

# Create your views here.

def course_detail_view(request):
    obj = Course.objects.get(id=4)
    Course.objects.create(code=12000, days = 'MWF', starttime=200, endtime=400, location='MDE AUD')
    '''
    context = {
        'code': obj.code,
        'location': obj.location,
        'days':obj.days
    }
    '''
    context={
        'object':obj
    }
    return render(request, 'course/detail.html', context)