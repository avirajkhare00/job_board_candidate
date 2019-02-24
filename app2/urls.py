from django.urls import path
from app2.views import register_page, employer_jobs_page, new_job, login_page, logout_page, show_candidates
from app2.api import apply_job_api

urlpatterns = [
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('jobs/', employer_jobs_page, name='employer_jobs_page'),
    path('new_job/', new_job, name='new_job'),
    path('view_candidates/', show_candidates, name='show_candidates'),
    #api path below
    path('api/v1/apply_job/', apply_job_api, name='apply_job_api'),
]
