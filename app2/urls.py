from django.urls import path
from app2.views import register_page, employer_jobs_page, new_job, login_page, logout_page

urlpatterns = [
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('jobs/', employer_jobs_page, name='employer_jobs_page'),
    path('new_job/', new_job, name='new_job')
]
