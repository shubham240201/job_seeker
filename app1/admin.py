

# Register your models here.
from django.contrib import admin
from .models import JobSeeker, Resume

admin.site.register(JobSeeker)
admin.site.register(Resume)
