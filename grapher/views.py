from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_graph(request):
    return render(request, 'index.html')