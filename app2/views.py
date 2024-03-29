from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from app2.core.auth_modules.validate_signup import ValidateSignup
from app2.core.job_modules.store_new_job import StoreNewJob
from app2.core.job_modules.update_job import UpdateJobById
from app2.models import CompanyDetails, JobPost, JobSkills, JobApplicants, HomeRecruiter
from app.models import CandidateFields
from common_app.models import GoogleRecaptchaPages, GoogleRecaptchaSiteKey
import requests

from job_board_candidate.settings import GOOGLE_RECAPTCHA_SECRET_KEY

# Create your views here.


def index_page(request):

    if request.method == 'GET':

        return render(request, 'html2/index.html')

    if request.method == 'POST':

        return HttpResponse(401)


def register_page(request):

    if request.method == 'GET':

        return render(request, 'html2/register.html', {
            'status': 'ok',
            'site_key': GoogleRecaptchaSiteKey.objects.get(config_id=1).site_key,
            'page_name': GoogleRecaptchaPages.objects.get(config_id=2).page_name
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

            if ValidateSignup(request.POST).validate_it() == 'ok':

                user = authenticate(request, username=request.POST['employer_username'],
                                password=request.POST['employer_password'])

                login(request, user)

                return redirect('../jobs/')

        else:

            return redirect('../register/?error=some_error')


def employer_jobs_page(request):

    if request.user.is_authenticated:

        company_name = CompanyDetails.objects.get(company_id__username=request.user.username)

        all_jobs_posted = JobPost.objects.filter(job_id=company_name, is_active=True)

        return render(request, 'html2/create_a_job.html', {
            'company_name': company_name.company_name,
            'active_job_number': len(all_jobs_posted),
            'all_jobs_posted': all_jobs_posted
        })

    else:

        return redirect('../login/?error=login_required')


def edit_job(request):

    if request.method == 'GET':

        if request.user.is_authenticated:

            if 'job_id' in request.GET:

                try:

                    if JobPost.objects.get(id=request.GET['job_id']).job_id.company_id.username == request.user.username:

                        job_post = JobPost.objects.get(id=request.GET['job_id'])
                        all_skills = []

                        for skill in JobSkills.objects.filter(job_id=job_post):

                            all_skills.append(skill.job_skill_id)

                        return render(request, 'html2/edit_job.html', {
                            "job_id": job_post.id,
                            "job_title_value": job_post.job_name,
                            "job_role_value": job_post.job_name_id,
                            "job_location": job_post.job_location_id,
                            "job_description": job_post.job_description,
                            "skill_ids": all_skills
                        })

                    else:

                        return HttpResponse('invalid job id')

                except JobPost.DoesNotExist:

                    return HttpResponse('job id does not exist')

            else:

                return redirect('../jobs/')

        else:

            return redirect('../login/')

    if request.method == 'POST':

        if request.user.is_authenticated:

            print(request.POST)

            if 'job_id' in request.POST:

                try:

                    if JobPost.objects.get(id=request.POST['job_id']).job_id.company_id.username == request.user.username:

                        UpdateJobById(request.POST, request.POST['job_id']).update_job()

                        return HttpResponse(200)

                    else:

                        return HttpResponse(401)

                except JobPost.DoesNotExist:

                    return HttpResponse('job id does not exist')

            else:

                return HttpResponse(401)

        else:

            return HttpResponse(401)


def new_job(request):

    if request.method == 'GET':

        if request.user.is_authenticated:

            return render(request, 'html2/post_a_job.html')

        else:

            redirect('../login/?error=not_logged_in')

    if request.method == 'POST':

        if request.user.is_authenticated:

            # print(request.POST)

            status = StoreNewJob(request.POST, request.user.username).store_data()

            if status == 'ok':

                return HttpResponse(200)

            else:

                return HttpResponse(status)

        else:

            return HttpResponse(401)


def job_show_page(request):

    if request.method == 'GET':

        # print(request.path.split('/')[2])

        if JobPost.objects.filter(job_slug=request.path.split('/')[2]).exists():

            job_post = JobPost.objects.get(job_slug=request.path.split('/')[2])

            return render(request, 'html2/job_show_page.html', {
                'job_name': job_post.job_name,
                'company_name': job_post.job_id.company_name,
                'job_location': job_post.job_location_id,
                'job_description': job_post.job_description,
                'job_id': job_post.id,
                'is_active': job_post.is_active
            })

        else:

            return HttpResponse(404)

    if request.method == 'POST':

        return HttpResponse(401)


def show_candidates(request):

    if request.method == 'GET':

        if 'job_id' in request.GET:

            if JobPost.objects.filter(job_id__company_id__username=request.user.username).exists() and JobPost.objects.filter(id=int(request.GET['job_id'])).exists():

                candidates_dict = []

                for candidate in JobApplicants.objects.filter(job_id=int(request.GET['job_id'])):

                    candidates_dict.append({
                        'first_name':  CandidateFields.objects.get(user_id__email=candidate.applicant_email).user_id.first_name,
                        'email': candidate.applicant_email,
                        'applied_on': candidate.applied_on,
                        'resume_link': '../../../static/resumes/' + CandidateFields.objects.get(user_id__email=candidate.applicant_email).resume_file_name
                    })

                return render(request, 'html2/view_candidates.html', {
                    'candidate_data': candidates_dict,
                    'job_name': JobPost.objects.get(id=int(request.GET['job_id'])).job_name,
                    'job_location': JobPost.objects.get(id=int(request.GET['job_id'])).job_location_id
                })

            if HomeRecruiter.objects.filter(recruiter_id__username=request.user.username).exists():

                candidates_dict = []

                for candidate in JobApplicants.objects.filter(job_id=int(request.GET['job_id'])):

                    candidates_dict.append({
                        'first_name':  CandidateFields.objects.get(user_id__email=candidate.applicant_email).user_id.first_name,
                        'email': candidate.applicant_email,
                        'applied_on': candidate.applied_on,
                        'resume_link': '../../../static/resumes/' + CandidateFields.objects.get(user_id__email=candidate.applicant_email).resume_file_name
                    })

                return render(request, 'html2/view_candidates.html', {
                    'candidate_data': candidates_dict,
                    'job_name': JobPost.objects.get(id=int(request.GET['job_id'])).job_name,
                    'job_location': JobPost.objects.get(id=int(request.GET['job_id'])).job_location_id
                })

    else:

        return HttpResponse(401)


def login_page(request):

    if request.method == 'GET':

        return render(request, 'html2/login.html')

    if request.method == 'POST':

        email = request.POST['employer_email']
        password = request.POST['employer_password']

        if User.objects.filter(email=email).exists():

            user = authenticate(request, username=User.objects.get(email=email).username, password=password)

            if user is not None:

                login(request, user)

                return redirect('../jobs/')

            else:

                return redirect('../login/?error=wrong_credentials')

        else:

            return redirect('../login?error=user_does_not_exists')


def logout_page(request):

    if request.method == 'GET':

        if request.user.is_authenticated:

            logout(request)

            return redirect('../login/')

        else:

            return redirect('../login/')

    if request.method == 'POST':

        return HttpResponse(401)
