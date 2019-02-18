from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class CandidateFields(models.Model):

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    candidate_status = models.IntegerField()
    candidate_job_id = models.IntegerField(null=True, blank=True)
    current_location_id = models.CharField(max_length=200, null=True, blank=True)
    remote_working = models.BooleanField(default=True)
    resume_file_name = models.CharField(max_length=200, null=True, blank=True)
    event_subscribe = models.BooleanField(default=True)
    newsletter_subscribe = models.BooleanField(default=True)

    def __str__(self):

        return self.user_id.username


class CandidateSkills(models.Model):

    user_id = models.ForeignKey(CandidateFields, on_delete=models.CASCADE)
    skill_id = models.CharField(max_length=10)

    def __str__(self):

        return self.user_id.user_id.username


class JobCategory(models.Model):

    job_category_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):

        return self.name


class JobName(models.Model):

    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    job_name_id = models.IntegerField()
    job_name = models.CharField(max_length=200)
    job_name_slug = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):

        return self.job_name


class PrimarySkills(models.Model):

    associated_to_job = models.ForeignKey(JobName, on_delete=models.CASCADE)
    primary_skill_id = models.IntegerField()
    name = models.CharField(max_length=200)

    def __str__(self):

        return self.name


class SecondarySkills(models.Model):

    associated_to_primary_skill = models.ForeignKey(PrimarySkills, on_delete=models.CASCADE)
    secondary_skill_id = models.IntegerField()
    name = models.CharField(max_length=200)

    def __str__(self):

        return self.name


class UserGeneratedSkills(models.Model):

    skill_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):

        return self.name


class IndustryType(models.Model):

    industry_type_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):

        return self.name


class CollegeDegrees(models.Model):

    college_degree_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    slug_name = models.CharField(max_length=200)

    def __str__(self):

        return self.slug_name


class CollegeSpecializations(models.Model):

    college_specialization_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    slug_name = models.CharField(max_length=200)

    def __str__(self):

        return self.slug_name


class CollegeNames(models.Model):

    college_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):

        return self.name


class IndianCityName(models.Model):

    city_name = models.CharField(max_length=200)
    city_value = models.CharField(max_length=200)

    def __str__(self):

        return self.city_name


class CompanyName(models.Model):

    company_name = models.CharField(max_length=200)
    company_name_slug = models.CharField(max_length=200)

    def __str__(self):

        return self.company_name


class CandidateInterestedCities(models.Model):

    user_id = models.ForeignKey(CandidateFields, on_delete=models.CASCADE)
    interested_city_value = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):

        return self.user_id.user_id.username
