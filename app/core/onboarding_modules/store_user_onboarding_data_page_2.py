from app.models import CandidateFields, CandidateInterestedCities
from app.models import IndianCityName
from app.core.onboarding_modules.save_pdf_file import SavePDFFile


class StoreOnboardingUserDataPage2:

    def __init__(self, request):

        self.request = request
        self.post_data = self.request.POST

    def store_data(self):

        if CandidateFields.objects.filter(user_id__username=self.request.user.username).exists():

            # if 'candidate_resume' not in self.request.FILES:
            #    return 'resume_not_found_error'

            if 'current_city' not in self.post_data:
                return 'current_city_not_found_error'

            if 'open_to_city[]' not in self.post_data:
                return 'interested_city_not_found_error'

            if 'remote_working_status' not in self.post_data:
                return 'remote_working_not_found_error'

            old_candidate = CandidateFields.objects.get(user_id__username=self.request.user.username)

            old_candidate.current_location_id = self.post_data['current_city']

            if self.post_data['remote_working_status'] == 'yes':
                old_candidate.remote_working = True

            if self.post_data['remote_working_status'] == 'no':
                old_candidate.remote_working = False

            if 'candidate_resume' in self.request.FILES:
                old_candidate.resume_file_name = SavePDFFile(self.request.FILES['candidate_resume']).save_file()

            if 'candidate_resume' not in self.request.FILES and old_candidate.onboarding_step_2_completed == False:
                old_candidate.resume_file_name = 'no_resume'  # TODO remember this. If user applies for job and no_resume is there then send alert

            if 'current_city' in self.post_data:

                if '_' in self.post_data['current_city']:

                    if self.post_data['current_city'].split('_')[0] == 'ucity':

                        new_city = IndianCityName()
                        new_city.city_name = self.post_data['current_city'].split('_')[1]
                        new_city.city_value = self.post_data['current_city'].split('_')[1]

                        new_city.save()

                    else:

                        old_candidate.current_location_id = self.post_data['current_city']

                else:

                    old_candidate.current_location_id = self.post_data['current_city']

            old_candidate.save()

            preferred_cities = self.post_data.getlist('open_to_city[]')

            if CandidateInterestedCities.objects.filter(user_id__user_id__username=self.request.user.username).exists():
                CandidateInterestedCities.objects.filter(user_id__user_id__username=self.request.user.username).delete()

            for p in preferred_cities:

                if '_' in p:
                    add_new_city = IndianCityName()

                    add_new_city.city_name = p.capitalize()
                    add_new_city.city_value = p

                    add_new_city.save()

                new_city = CandidateInterestedCities()

                new_city.user_id = old_candidate
                new_city.interested_city_value = p.capitalize()

                new_city.save()

            old_candidate.onboarding_step_2_completed = True

            old_candidate.save()

            return 2

        else:

            return "send_user_page_1"
