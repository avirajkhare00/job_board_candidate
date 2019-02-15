from django.contrib import admin
from app.models import JobName, JobCategory, PrimarySkills, SecondarySkills
from app.models import IndustryType, CollegeDegrees, CollegeSpecializations
from app.models import CandidateFields

# Register your models here.


admin.site.register(JobName)
admin.site.register(JobCategory)
admin.site.register(PrimarySkills)
admin.site.register(SecondarySkills)
admin.site.register(IndustryType)
admin.site.register(CollegeSpecializations)
admin.site.register(CollegeDegrees)
admin.site.register(CandidateFields)