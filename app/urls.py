from django.urls import path, include
from app.views import register_page, user_onboard, login_user, logout_user, candidate_jobs, candidate_profile
from app.views import candidate_settings
from app.api import check_candidate_email, fetch_job_functions, fetch_primary_skills, fetch_secondary_skills
from app.api import fetch_specialization_and_college_data, fetch_job_categories, get_suggested_skills
from app.api import get_primary_secondary_skills, fetch_indian_city_data, get_indian_cities, get_user_profile_data
from app.api import get_skill_name_from_id
urlpatterns = [
    path('register/', register_page, name='register_page'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('onboard/', user_onboard, name='user_onboard_zero'),
    path('jobs/', candidate_jobs, name='get_user_profile_data'),
    path('profile/', candidate_profile, name='candidate_profile'),
    path('settings/', candidate_settings, name='candidate_settings'),
    #api urls below
    path('fetch_job_categories/', fetch_job_categories, name='fetch_job_categories'),
    path('get_suggested_skills/', get_suggested_skills, name='get_suggested_skills'),
    path('get_primary_secondary_skills/', get_primary_secondary_skills, name='get_primary_secondary_skills'),
    path('get_indian_cities/', get_indian_cities, name='get_indian_cities'),
    path('get_user_profile_data/', get_user_profile_data, name='get_user_profile_data'),
    path('get_skill_name_id/', get_skill_name_from_id, name='get_skill_name_id'),
    #remove all apis after data is offloded in prod
    path('fetch_job_function_data/', fetch_job_functions, name='fetch_job_functions'),
    path('fetch_primary_skills_data/', fetch_primary_skills, name='fetch_primary_skills'),
    path('fetch_secondary_skills_data/', fetch_secondary_skills, name='fetch_secondary_skills'),
    path('fetch_specialization_and_college_data/', fetch_specialization_and_college_data, name='fetch_specialization_and_college_data'),
    path('fetch_indian_city_data/', fetch_indian_city_data, name='fetch_indian_city_data')
]