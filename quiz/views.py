from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Choice
from .forms import QuizForm, QuestionForm, ChoiceForm

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz})

def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save()
            return redirect('quiz_detail', quiz_id=quiz.id)
    else:
        form = QuizForm()
    return render(request, 'quiz/create_quiz.html', {'form': form})

def create_question(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            return redirect('quiz_detail', quiz_id=quiz.id)
    else:
        form = QuestionForm()
    return render(request, 'quiz/create_question.html', {'form': form, 'quiz': quiz})

def create_choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.question = question
            choice.save()
            return redirect('quiz_detail', quiz_id=question.quiz.id)
    else:
        form = ChoiceForm()
    return render(request, 'quiz/create_choice.html', {'form': form, 'question': question})

# Create your views here.
