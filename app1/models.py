from django.db import models

class JobSeeker(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

class Resume(models.Model):
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return f'{self.jobseeker.full_name} Resume'
