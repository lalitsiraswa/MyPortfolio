import contextlib
from typing import ContextManager
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from .models import Project, Skill, Tag, Message, Endorsement, Comment
from .forms import ProjectForm, MessageForm, SkillForm, EndorsementForm, CommentForm, QuestionForm
from django.contrib import messages

# Create your views here.
def homePage(request):
    projects = Project.objects.all()
    detailedskills = Skill.objects.exclude(body='')

    skills = Skill.objects.filter(body='')
    endorsement = Endorsement.objects.all().filter(approved=True)

    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Message Was Successfully Sent!")


    context = {
        'projects':projects, 
        'skills':skills,
        'detailedskills':detailedskills,
        'form': form,
        'endorsement': endorsement
    }
    return render(request, 'base/home.html', context=context)

def projectPage(request, pk):
    project = Project.objects.get(id=pk)

    count = project.comment_set.count()

    comments = project.comment_set.all().order_by('-created')

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # Assign the form object without saving
            comment.project = project # Assign the project to comment
            comment.save() 
            messages.success(request, "Your Comment Was Successfully Added!")
            # print(form)
            # return redirect('home')

    context = {
        'project': project,
        'count': count,
        'comments': comments,
        'form': form
    }
    return render(request, 'base/project.html', context=context)

def addProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # print(form)
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'base/project_form.html', context)
    

def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            # pritn(form)
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'base/project_form.html', context)
    
def inboxPage(request):
    inbox = Message.objects.all().order_by('-is_read')
    unreadCount = Message.objects.filter(is_read=False).count()
    context = {
        'inbox': inbox,
        'unreadCount': unreadCount
    }
    return render(request, 'base/inbox.html', context=context)

def messagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {
        'message': message
    }
    return render(request, 'base/message.html', context=context)

def addSkill(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Skill Was Successfully Added!")
            return redirect('home')
    context = {
        'form': form
    }   
    return render(request, 'base/skill_form.html', context=context)

def addEndorsement(request):
    form = EndorsementForm()
    if request.method == 'POST':
        form = EndorsementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank You, Your Endorsement Was Successfully Added!")
            return redirect('home')
    context = {
        'form': form
    }   
    return render(request, 'base/endorsement_form.html', context=context)

def donationPage(request):
    return render(request, 'base/donation.html')

def chartPage(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank You For Your Vote!")
            return redirect('chart')
    context = {
        'form': form
    }
    return render(request, 'base/chart.html', context=context)