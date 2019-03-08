from django.urls import path
from app2.views import register_page, employer_jobs_page, new_job, login_page, logout_page, show_candidates
from app2.api import apply_job_api, fetch_job_ids, fetch_job_by_id, fetch_recent_jobs
from app2.core.home_recruiter_modules.api import fetch_job_id_recruiter
from app2.core.home_recruiter_modules.views import recruiter_login_page, recruiter_jobs_page, recruiter_job_add_page


urlpatterns = [
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('jobs/', employer_jobs_page, name='employer_jobs_page'),
    path('new_job/', new_job, name='new_job'),
    path('view_candidates/', show_candidates, name='show_candidates'),
    #url path for inhouse recruiter login
    path('recruiter_login/', recruiter_login_page, name='recruiter_login_page'),
    path('recruiter_jobs_page/', recruiter_jobs_page, name='recruiter_jobs_page'),
    path('recruiter_job_add_page/', recruiter_job_add_page, name='recruiter_job_add_page/'),
    #api path below
    path('api/v1/apply_job/', apply_job_api, name='apply_job_api'),
    path('api/v1/fetch_job_ids/', fetch_job_ids, name='fetch_job_ids'),
    path('api/v1/fetch_job_by_id/', fetch_job_by_id, name='fetch_job_by_id'),
    path('api/v1/fetch_recent_job_ids/', fetch_recent_jobs, name='fetch_recent_jobs'),
    path('api/v1/fetch_recruiter_job_ids/', fetch_job_id_recruiter, name='fetch_job_id_recruiter')
]
