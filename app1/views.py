from django.shortcuts import render, redirect
from .forms import JobSeekerForm, ResumeForm
from .models import JobSeeker,Resume
from django.contrib import messages

import pathlib

def to_path(directory):
    if callable(directory):
        directory = directory()
    return pathlib.Path(directory)

def home(request):
    if request.method == 'POST':
        jobseeker_form = JobSeekerForm(request.POST)
        resume_form = ResumeForm(request.POST, request.FILES)
        if jobseeker_form.is_valid() and resume_form.is_valid():
            jobseeker = jobseeker_form.save()
            resume = resume_form.save(commit=False)
            resume.jobseeker = jobseeker
            resume.save()
            messages.suceess(request,f'Thank you for submitting your information,{jobseeker.full_name}!')
            return redirect('dashboard')
    else:
        jobseeker_form = JobSeekerForm()
        resume_form = ResumeForm()
    return render(request, 'home.html', {'jobseeker_form': jobseeker_form, 'resume_form': resume_form})

def dashboard(request):
    jobseeker = JobSeeker.objects.get(pk=request.user.pk)
    resumes =Resume.objects.filter(jobseeker=jobseeker)
    return render(request, 'dashboard.html', {'jobseeker': jobseeker, 'resumes': resumes})
