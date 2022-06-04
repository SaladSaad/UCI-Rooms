from django.shortcuts import render
from django.http import HttpResponse

from .models import Course

# Create your views here.
def show_graph(request):
    context = {"nani":'bruh', "mylist":['nothing at all','wubba lubba dub dub',120345]}
    return render(request, 'index.html', context)

# Create your views here.

def course_detail_view(request):
    obj = Course.objects.get(id=1)
    context = {
        'Code': obj.code,
        'location': obj.location
    }
    return render(request, 'course/detail.html', {})