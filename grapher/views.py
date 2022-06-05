from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import Course

# Create your views here.
def show_graph_view(request):
    json_serializer = serializers.get_serializer("json")()
    courses_json = json_serializer.serialize(Course.objects.all())
    
    context = {'data': courses_json}
    return render(request, 'index.html', context)

# Create your views here.

def course_detail_view(request):
    
    obj=Course.objects.get(code = 17888)
    
    context = {
        'object':obj
    }
    return render(request, 'course/detail.html', context)