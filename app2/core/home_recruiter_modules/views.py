from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from app2.core.home_recruiter_modules.auth_user.auth_user import AuthUser
from app2.core.home_recruiter_modules.store_data_modules.store_data import StoreRecruiterJobData


def recruiter_login_page(request):

    if request.method == 'GET':

        return render(request, 'html2/inhouse_recruiter_login.html')

    if request.method == 'POST':

        if 'employer_email' not in request.POST:

            return redirect('../recruiter_login/?error=email_not_given')

        elif 'employer_password' not in request.POST:

            return redirect('../recruiter_login?error=password_not_given')

        else:

            state = AuthUser(request).check_and_auth_user()

            if state == 'user_logged_in':

                return redirect('../recruiter_jobs_page/')

            elif state == 'permission_issue':

                return redirect('../recruiter_login?error=permission_issue')

            elif state == 'user_not_exist':

                return redirect('../recruiter_login?error=user_does_not_exist')

            elif state == 'password_incorrect':

                return redirect('../recruiter_login/?error=password_incorrect')


def recruiter_jobs_page(request):

    if request.method == 'GET':

        if request.user.is_authenticated:

            return render(request, 'html2/inhouse_recruiter_jobs_page.html')

        else:

            return redirect('../recruiter_login/')


def recruiter_job_add_page(request):

    if request.method == 'GET':
    
        if request.user.is_authenticated:

            return render(request, 'html2/inhouse_recruiter_add_job.html')

        else:

            return redirect('../recruiter_login/?error=user_not_logged_in')

    if request.method == 'POST':

        if request.user.is_authenticated:

            StoreRecruiterJobData(request).store_data()

            return HttpResponse(200)

        else:

            return HttpResponse(401)


