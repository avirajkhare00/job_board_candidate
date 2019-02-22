from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CompanyDetails(models.Model):

    company_id = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=300)

    def __str__(self):

        return self.company_name


class JobPost(models.Model):

    job_id = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=500)
    job_slug = models.CharField(max_length=700)
    job_name_id = models.IntegerField()
    job_location_id = models.CharField(max_length=200, null=True, blank=True)
    is_remote_friendly = models.BooleanField(default=False)
    job_description = models.TextField()
    is_active = models.BooleanField(default=True)
    is_draft = models.BooleanField(default=False)

    def __str__(self):

        return self.job_id.company_name


class JobSkills(models.Model):

    job_id = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    job_skill_id = models.CharField(max_length=10)

    def __str__(self):

        return self.job_id.job_id.company_name
