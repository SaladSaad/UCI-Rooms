from django.shortcuts import render
from django.http import HttpResponse

from .models import Course

# Create your views here.
def show_graph(request):
    return render(request, 'index.html')

# Create your views here.

def course_detail_view(request):
    obj = Course.objects.get(id=1)
    context = {
        'Code': obj.code,
        'location': obj.location
    }
    return render(request, 'course/detail.html', {})