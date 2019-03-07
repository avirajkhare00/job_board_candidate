from django.contrib import admin
from app2.models import JobPost, JobApplicants, CompanyDetails, HomeRecruiter
# Register your models here.

admin.site.register(CompanyDetails)
admin.site.register(JobPost)
admin.site.register(JobApplicants)
admin.site.register(HomeRecruiter)
