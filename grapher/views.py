from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from numpy import sort

from .models import Course
from .forms import chartForm

# Create your views here.


def show_graph_view(request, **kwargs):

    ### Setting up chart form ###
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = chartForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            formLocation = form.cleaned_data['location']
            formDay = form.cleaned_data['day']
            formQuarter = form.cleaned_data['quarter']
            formSort = form.cleaned_data['sort']

            json_serializer = serializers.get_serializer("json")()
            if len(formLocation) > 0:
                courses_json = json_serializer.serialize(
                    Course.objects.all().filter(location=formLocation, days=formDay).order_by(formSort))
                context = {'qs': courses_json, 'form': form}
                return render(request, 'index.html', context)
            else:
                courses_json = json_serializer.serialize(
                    Course.objects.all().filter(days=formDay).order_by(formSort))
                context = {'qs': courses_json, 'form': form}
                return render(request, 'index.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = chartForm()
    ###

    ### Filling Chart ###
    json_serializer = serializers.get_serializer("json")()
    courses_json = json_serializer.serialize(
        Course.objects.all().filter(days="W").order_by('location'))
    context = {'qs': courses_json, 'form': form}
    return render(request, 'index.html', context)
    ###


def course_detail_view(request):

    obj = Course.objects.get(code=17888)

    context = {
        'object': obj
    }
    return render(request, 'course/detail.html', context)
