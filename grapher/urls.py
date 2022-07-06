from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_graph_view),
    path('chart/', views.show_graph_view),
    path('course/', views.course_detail_view)
]