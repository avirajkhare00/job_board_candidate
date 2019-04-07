from django.contrib.auth.models import User
from app.models import CandidateFields, CandidateSkills, JobName, CandidateInterestedCities


class GetUserProfileData:

    def __init__(self, username):

        self.username = username
        self.profile_data = {}

    def fetch_user_data(self):

        user_model_object = User.objects.get(username=self.username)

        if CandidateFields.objects.filter(user_id__username=self.username).exists():

            candidate_field_object = CandidateFields.objects.get(user_id__username=self.username)
            candidate_skills_list = CandidateSkills.objects.filter(user_id__user_id__username=self.username)
            candidate_interested_cities_query = CandidateInterestedCities.objects.filter(user_id__user_id__username=self.username)

            candidate_skills_list_list = []
            candidate_interested_cities = []

            for c in candidate_skills_list:

                candidate_skills_list_list.append(c.skill_id)

            for c in candidate_interested_cities_query:

                candidate_interested_cities.append(c.interested_city_value)

            self.profile_data = {
                'status': True,
                'first_name': user_model_object.first_name,
                'last_name': user_model_object.last_name,
                'email': user_model_object.email,
                'candidate_status': candidate_field_object.candidate_status,
                'candidate_job_title': JobName.objects.get(job_name_id=candidate_field_object.candidate_job_id).job_name,
                'candidate_job_value': candidate_field_object.candidate_job_id,
                'current_location_value': candidate_field_object.current_location_id,
                'remote_working_status': candidate_field_object.remote_working,
                # 'candidate_resume_url': candidate_field_object.resume_file_name,
                'candidate_interested_cities': candidate_interested_cities,
                'candidate_skill_ids': candidate_skills_list_list,
                'event_subscribe_status': candidate_field_object.event_subscribe,
                'newsletter_subscribe_status': candidate_field_object.newsletter_subscribe
            }

            if candidate_field_object.resume_file_name == 'no_resume':

                self.profile_data['candidate_resume_url'] = 'no_resume'

            else:

                self.profile_data['candidate_resume_url'] = candidate_field_object.resume_file_name

            return self.profile_data

        else:

            self.profile_data['status'] = False

            return self.profile_data
