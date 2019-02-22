from django.shortcuts import render, HttpResponse, redirect
from app.core.auth_modules.validate_signup import ValidateSignup
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from app.core.onboarding_modules.store_onboarding_user_data import StoreOnboardingUserData
from app2.models import JobPost
from app.models import CandidateFields
import json

# Create your views here.


def register_page(request):

    if request.method == 'GET':

        return render(request, 'html/register.html', {'status': 'ok'})

    if request.method == 'POST':

        signup_status = ValidateSignup(request.POST).validate_it()

        if signup_status == 'ok':

            user = authenticate(request, username=request.POST['candidate_username'], password=request.POST['candidate_password'])

            login(request, user)

            return redirect('../onboard/?page=1')

        return render(request, 'html/register.html')


def login_user(request):

    if request.method == 'GET':

        return render(request, 'html/login.html')

    if request.method == 'POST':

        email = request.POST['candidate_email']
        password = request.POST['candidate_password']

        if User.objects.filter(email=email).exists():

            user = authenticate(request, username=User.objects.get(email=email).username, password=password)

            if user is not None:

                login(request, user)

                return redirect('../jobs/')

            else:

                return redirect('../login/?error=wrong_credentials')

        else:

            return redirect('../login?error=wrong_credentials')


def logout_user(request):

    if request.user.is_authenticated:

        logout(request)

        return redirect('../login/')

    else:

        return redirect('../login/')


def candidate_jobs(request):

    if request.user.is_authenticated:

        all_jobs = JobPost.objects.filter(job_name_id=CandidateFields.objects.get(user_id__username=request.user.username).candidate_job_id, is_active=True)

        print(all_jobs)

        return render(request, 'html/jobs.html', {
            'all_jobs': all_jobs
        })

    else:

        return redirect('../login/?error=user_not_logged_in')


def candidate_profile(request):

    if request.user.is_authenticated:

        return render(request, 'html/profile.html')

    else:

        return redirect('../login/?error=user_not_logged_in')


def candidate_settings(request):

    if request.user.is_authenticated:

        return render(request, 'html/settings.html')

    else:

        return redirect('../login/?error=user_not_logged_in')


def user_onboard(request):

    if request.method == 'GET':

        if request.user.is_authenticated:

            if 'page' in request.GET and request.GET['page'] == '1':

                return render(request, 'html/candidate_onboard_0.html')

            if 'page' in request.GET and request.GET['page'] == '2':

                return render(request, 'html/candidate_onboard_1.html')

            if 'page' in request.GET and request.GET['page'] == '3':

                return render(request, 'html/candidate_onboard_2.html')

            if 'page' not in request.GET:

                return redirect('../onboard?page=1')

            else:

                return redirect('../onboard?page=1')

        else:

            return redirect('../login/')

    if request.method == 'POST':

        if request.user.is_authenticated:

            status = StoreOnboardingUserData(request).store_data()

            if status == "send_user_page_1":

                return redirect('../onboard/?page=1')

            if status == 1:

                return redirect('../onboard/?page=2')

            if status == 2:

                return redirect('../onboard/?page=3')

            if status == 3:

                return redirect('../jobs/')

