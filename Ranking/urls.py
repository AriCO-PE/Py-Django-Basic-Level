from django.urls import path
from . import views

urlpatterns = [
    path('ranking/', views.student_ranking, name='student_ranking'),
]
