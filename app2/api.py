from django.shortcuts import HttpResponse, redirect
from app.models import CandidateFields
from app2.core.job_modules.job_applicant_logic import JobApplicantLogin


def apply_job_api(request):

    if request.method == 'POST':

        if request.user.is_authenticated:

            if CandidateFields.objects.filter(user_id__username=request.user.username).exists():

                return HttpResponse(JobApplicantLogin(CandidateFields.objects.get(user_id__username=request.user.username).user_id.email, int(request.POST['job_id'])).store_job_applicant())

            else:

                return HttpResponse('complete_onboarding')

        else:

            return HttpResponse(401)
