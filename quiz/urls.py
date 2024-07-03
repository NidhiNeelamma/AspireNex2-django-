from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/new/', views.create_quiz, name='create_quiz'),
    path('quiz/<int:quiz_id>/question/new/', views.create_question, name='create_question'),
    path('question/<int:question_id>/choice/new/', views.create_choice, name='create_choice'),
]
