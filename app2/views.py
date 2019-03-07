from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from app2.core.auth_modules.validate_signup import ValidateSignup
from app2.core.job_modules.store_new_job import StoreNewJob
from app2.models import CompanyDetails, JobPost, JobSkills, JobApplicants, HomeRecruiter
from app.models import CandidateFields

# Create your views here.


def index_page(request):

    if request.method == 'GET':

        if request.user.is_authenticated:

            if CandidateFields.objects.filter(user_id__username=request.user.username).exists():

                return redirect('candidate/jobs/')

            if CompanyDetails.objects.filter(company_id__username=request.user.username).exists():

                return redirect('employer/jobs/')

        else:

            return render(request, 'html2/index.html')

    else:

        return HttpResponse(401)


def register_page(request):

    if request.method == 'GET':

        return render(request, 'html2/register.html')

    if request.method == 'POST':

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


def new_job(request):

    if request.method == 'GET':

        if request.user.is_authenticated:

            return render(request, 'html2/post_a_job.html')

        else:

            redirect('../login/?error=not_logged_in')

    if request.method == 'POST':

        if request.user.is_authenticated:

            print(request.POST)

            status = StoreNewJob(request.POST, request.user.username).store_data()

            if status == 'ok':

                return HttpResponse(200)

            else:

                return HttpResponse(status)

        else:

            return HttpResponse(401)


def job_show_page(request):

    if request.method == 'GET':

        print(request.path.split('/')[2])

        if JobPost.objects.filter(job_slug=request.path.split('/')[2]).exists():

            job_post = JobPost.objects.get(job_slug=request.path.split('/')[2])

            return render(request, 'html2/job_show_page.html', {
                'job_name': job_post.job_name,
                'company_name': job_post.job_id.company_name,
                'job_location': job_post.job_location_id,
                'job_description': job_post.job_description,
                'job_id': job_post.id
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

            return redirect('../login?error=wrong_credentials')


def logout_page(request):

    if request.method == 'GET':

        if request.user.is_authenticated:

            logout(request)

            return redirect('../login/')

        else:

            return redirect('../login/')

    if request.method == 'POST':

        return HttpResponse(401)
