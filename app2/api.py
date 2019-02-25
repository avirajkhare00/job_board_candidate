from django.shortcuts import HttpResponse, redirect
from app.models import CandidateFields
from app2.models import JobPost, CompanyDetails
from app2.core.data_components.fetch_job_ids import FetchJobIds
from app2.core.job_modules.job_applicant_logic import JobApplicantLogin
from app2.core.data_components.fetch_job_by_id import FetchJobById
import json


def apply_job_api(request):

    if request.method == 'POST':

        if request.user.is_authenticated:

            if CandidateFields.objects.filter(user_id__username=request.user.username).exists():

                return HttpResponse(JobApplicantLogin(CandidateFields.objects.get(user_id__username=request.user.username).user_id.email, int(request.POST['job_id'])).store_job_applicant())

            else:

                return HttpResponse('complete_onboarding')

        else:

            return HttpResponse(401)


def fetch_job_ids(request):

    if request.method == 'GET':

        if request.user.is_authenticated:

            if CompanyDetails.objects.filter(company_id__username=request.user.username).exists():

                return HttpResponse(
                    json.dumps({
                        'data': FetchJobIds(request.user.username).fetch_ids()
                    }),
                    content_type='application/json'
                )
            else:

                return HttpResponse(401)

        else:

            return HttpResponse(401)


def fetch_job_by_id(request):

    if request.method == 'GET':

        if request.user.is_authenticated:

            if CompanyDetails.objects.filter(company_id__username=request.user.username):

                if 'job_id' in request.GET:

                    if JobPost.objects.filter(id=request.GET['job_id']).exists():

                        if JobPost.objects.get(id=request.GET['job_id']).job_id.company_id.username == request.user.username:

                            return HttpResponse(
                                json.dumps({
                                    'data': FetchJobById(request.GET['job_id']).get_data()
                                }),
                                content_type='application/json'
                            )

                        else:

                            return HttpResponse(401)

                    else:

                        return HttpResponse(401)

                else:

                    return HttpResponse(401)

            else:

                return HttpResponse(401)

        else:

            return HttpResponse(401)

    else:

        return HttpResponse(401)
