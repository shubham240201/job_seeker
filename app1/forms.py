
from django import forms
from .models import JobSeeker, Resume

class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = ('full_name', 'email', 'phone')

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('file',)
