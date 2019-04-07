from django.shortcuts import render, HttpResponse, redirect
from app.core.auth_modules.validate_signup import ValidateSignup
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from common_app.models import GoogleRecaptchaSiteKey, GoogleRecaptchaPages
from app.core.onboarding_modules.store_user_onboarding_data_page_1 import StoreUserOnboardingDataPage1
from app.core.onboarding_modules.store_user_onboarding_data_page_2 import StoreOnboardingUserDataPage2
from app.core.onboarding_modules.store_user_onboarding_data_page_3 import StoreOnboardingUserDataPage3
import requests

from job_board_candidate.settings import GOOGLE_RECAPTCHA_SECRET_KEY

# Create your views here.


def register_page(request):

    if request.method == 'GET':

        return render(request, 'html/register.html', {
            'status': 'ok',
            'site_key': GoogleRecaptchaSiteKey.objects.get(config_id=1).site_key,
            'page_name': GoogleRecaptchaPages.objects.get(config_id=1).page_name
        })

    if request.method == 'POST':

        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        ''' End reCAPTCHA validation '''

        if result['success']:

            signup_status = ValidateSignup(request.POST).validate_it()

            if signup_status == 'ok':
                user = authenticate(request, username=request.POST['candidate_username'],
                                    password=request.POST['candidate_password'])

                login(request, user)

                return redirect('../onboard/?page=1')

            return render(request, 'html/register.html', {'status': signup_status})

        else:

            return render(request, 'html/register.html', {'status': 'recaptcha_error'})


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

            return redirect('../login?error=user_does_not_exists')


def logout_user(request):

    if request.user.is_authenticated:

        logout(request)

        return redirect('../login/')

    else:

        return redirect('../login/')


def candidate_jobs(request):

    if request.user.is_authenticated:

        return render(request, 'html/jobs.html')

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

            if request.POST['page'] == '0':

                status_1 = StoreUserOnboardingDataPage1(request).store_data()

                if status_1 == 1:

                    return redirect('../onboard/?page=2')

                else:

                    return redirect('../onboard/?page=1&error=' + str(status_1))

            if request.POST['page'] == '1':

                status_2 = StoreOnboardingUserDataPage2(request).store_data()

                if status_2 == 2:

                    return redirect('../onboard/?page=3')

                if status_2 == 'send_user_page_1':

                    return redirect('../onboard/?page=1')

                else:

                    return redirect('../onboard/?page=2&error=' + str(status_2))

            if request.POST['page'] == '2':

                status_3 = StoreOnboardingUserDataPage3(request).store_data()

                if status_3 == 3:

                    return redirect('../jobs/')

                if status_3 == 'send_user_page_1':

                    return redirect('../onboard/?page=1')

                else:

                    return redirect('../onboard/?page=3&error=' + str(status_3))

        else:

            return HttpResponse(401)
