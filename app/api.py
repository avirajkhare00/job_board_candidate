from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from app.core.utils.fetch_job_functions import FetchJobFunctions
from app.core.utils.fetch_primary_skills import FetchPrimarySkills
from app.core.utils.fetch_secondary_skills import FetchSecondarySkills
from app.core.utils.fetch_industry_type import FetchIndustryType
from app.core.utils.fetch_degrees import FetchCollegeDegree
from app.core.utils.fetch_specializations import FetchCollegeSpecialization
from app.core.utils.fetch_cities_name_india import FetchCitiesNameIndia
from app.core.onboarding_modules.fetch_job_categories import FetchJobCategories
from app.core.onboarding_modules.fetch_suggested_skills import FetchSuggestedSkills
from app.core.onboarding_modules.get_primary_secondary_skills import GetPrimarySecondarySkills
from app.core.onboarding_modules.get_indian_city_names import GetIndianCityNames
import json


def check_candidate_email(request):

    if request.method == 'GET':

        if User.objects.filter(email=request.GET['email']).exists():

            return HttpResponse(json.dumps({"status": "not_ok"}))

        else:

            return HttpResponse(json.dumps({"status": "ok"}))


def fetch_job_functions(request):

    FetchJobFunctions().fetch_data()

    return HttpResponse(200)


def fetch_primary_skills(request):

    FetchPrimarySkills().fetch_skills()

    return HttpResponse(200)


def fetch_secondary_skills(request):

    FetchSecondarySkills().fetch_data()

    return HttpResponse(200)


def fetch_specialization_and_college_data(request):

    FetchIndustryType().fetch_data()
    FetchCollegeDegree().fetch_data()
    FetchCollegeSpecialization().fetch_data()

    return HttpResponse(200)


def fetch_indian_city_data(request):

    FetchCitiesNameIndia().fetch_data()

    return HttpResponse(200)


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


def get_indian_cities(request):

    if request.user.is_authenticated:

        return HttpResponse(
            json.dumps(GetIndianCityNames().get_data()),
            content_type='application/json'
        )

    else:

        return HttpResponse(401)