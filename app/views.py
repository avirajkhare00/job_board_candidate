from django.shortcuts import render, HttpResponse, redirect
from app.core.auth_modules.validate_signup import ValidateSignup
from django.contrib.auth import login, authenticate, logout
from app.core.onboarding_modules.store_onboarding_user_data import StoreOnboardingUserData
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

        return HttpResponse('login_page_coming_soon')

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            redirect('../')

        else:

            redirect('login/?error=wrong_credentials')


def logout_user(request):

    if request.user.is_authenticated:

        logout(request)

        return redirect('../login/')

    else:

        return redirect('../login/')


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

                return render(request, 'html/candidate_onboard_0.html')

        else:

            return redirect('../login/')

    if request.method == 'POST':

        if request.user.is_authenticated:

            status = StoreOnboardingUserData(request).store_data()

            print(status)

            if status == 1:

                return redirect('../onboard/?page=2')

            if status == 2:

                return redirect('../onboard/?page=3')

            return HttpResponse()
