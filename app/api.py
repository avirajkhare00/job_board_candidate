from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from app.core.utils.fetch_data_for_db import FetchDataForDb
from app.core.onboarding_modules.fetch_job_categories import FetchJobCategories
from app.core.onboarding_modules.fetch_suggested_skills import FetchSuggestedSkills
from app.core.onboarding_modules.get_primary_secondary_skills import GetPrimarySecondarySkills
from app.core.onboarding_modules.get_indian_city_names import GetIndianCityNames
from app.core.common_data.get_user_profile_data import GetUserProfileData
from app.core.common_data.get_skill_name_id import GetSkillNameId
from app.core.filter_jobs.filter_candidate_jobs import FilterCandidateJobs
import json


def fetch_data_for_db(request):

    if request.method == 'POST':

        if request.POST['number'] == '9893371444':

            if FetchDataForDb().fetch_data():

                return HttpResponse(200)

            else:

                return HttpResponse(500)

        else:

            return HttpResponse('invalid_code')

    else:

        return HttpResponse(401)


def fetch_job_categories(request):

    if request.user.is_authenticated:

        return HttpResponse(
            json.dumps(FetchJobCategories().fetch_categories()),
            content_type='application/json'
        )

    else:

        return HttpResponse(401)


def get_suggested_skills(request):

    if request.user.is_authenticated:

        return HttpResponse(
            json.dumps(FetchSuggestedSkills(request.GET).fetch_data()),
            content_type='application/json'
        )

    else:

        return HttpResponse(401)


def get_primary_secondary_skills(request):

    if request.user.is_authenticated:

        return HttpResponse(
            json.dumps(GetPrimarySecondarySkills().get_data()),
            content_type='application/json'
        )

    else:

        return HttpResponse(401)


def get_user_profile_data(request):

    if request.user.is_authenticated:

        return HttpResponse(
            json.dumps(GetUserProfileData(request.user.username).fetch_user_data()),
            content_type='application/json'
        )

    else:

        return HttpResponse(401)


def get_indian_cities(request):

    if request.user.is_authenticated:

        return HttpResponse(
            json.dumps(GetIndianCityNames().get_data()),
            content_type='application/json'
        )

    else:

        return HttpResponse(401)


def get_skill_name_from_id(request):

    if request.user.is_authenticated:

        return HttpResponse(
            json.dumps(GetSkillNameId(request.GET['skill_id']).get_skill_name()),
            content_type='application/json'
        )

    else:

        return HttpResponse(401)


def filter_candidate_jobs(request):

    if request.method == 'GET':

        if request.user.is_authenticated:

            return HttpResponse(
                json.dumps({
                    'status': 'ok',
                    'data': FilterCandidateJobs(request.user.username).filter_jobs()
                }),
                content_type='application/json'
            )

        else:

            return HttpResponse(401)

    if request.method == 'POST':

        return HttpResponse(401)
