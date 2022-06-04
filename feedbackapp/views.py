
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feedback
def home(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')

        Feedback.objects.create(name=name,email=email,feedback=feedback)
        return redirect('home')



    return render(request,'feedbackapp/index.html',{})


def feedbacks(request):
    context = {'feedbacks':Feedback.objects.all()}
    return render(request,'feedbackapp/feedbacks.html',context)


def about(request):
    return render(request,'feedbackapp/about.html',{})
