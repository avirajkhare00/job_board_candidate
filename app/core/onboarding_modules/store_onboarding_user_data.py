from app.models import CandidateFields, CandidateSkills, UserGeneratedSkills, CandidateInterestedCities
from django.core.files.storage import FileSystemStorage


class StoreOnboardingUserData:

    def __init__(self, request):

        self.request = request
        self.post_data = self.request.POST

    def store_data(self):

        print(self.post_data)

        if 'page' not in self.post_data:

            return 'page_not_found_error'

        if self.post_data['page'] == '0':

            if 'candidate_status' not in self.post_data:

                return 'candidate_status_not_found_error'

            if 'skills[]' not in self.post_data:

                return 'skills_not_found_error'

            if 'job_role' not in self.post_data:

                return 'job_role_not_found_error'

            if CandidateFields.objects.filter(user_id=self.request.user).exists():

                old_candidate = CandidateFields.objects.get(user_id=self.request.user)

                if self.post_data['candidate_status'] == 'professional':

                    old_candidate.candidate_status = 1

                if self.post_data['candidate_status'] == 'fresher':

                    old_candidate.candidate_status = 2

                old_candidate.candidate_job_id = int(self.post_data['job_role'])

                old_candidate.save()

                CandidateSkills.objects.filter(user_id=old_candidate).delete()

                # TODO think for better logic to update all skills

                for i in self.post_data.getlist('skills[]'):

                    if i.split('_')[0] == 'us':
                        new_skill = UserGeneratedSkills()

                        new_skill.skill_id = len(UserGeneratedSkills.objects.all()) + 1
                        new_skill.name = i.split('_')[1]

                        new_skill.save()

                        new_candidate_skills = CandidateSkills()

                        new_candidate_skills.user_id = old_candidate

                        print(str(new_skill.skill_id))

                        new_candidate_skills.skill_id = 'us_' + str(new_skill.skill_id)

                        new_candidate_skills.save()

                    else:

                        new_candidate_skills = CandidateSkills()

                        new_candidate_skills.user_id = old_candidate

                        new_candidate_skills.skill_id = i

                        new_candidate_skills.save()

            else:

                new_candidate = CandidateFields()

                new_candidate.user_id = self.request.user

                if self.post_data['candidate_status'] == 'professional':

                    new_candidate.candidate_status = 1

                if self.post_data['candidate_status'] == 'fresher':

                    new_candidate.candidate_status = 2

                new_candidate.candidate_job_id = int(self.post_data['job_role'])

                new_candidate.save()

                for i in self.post_data.getlist('skills[]'):

                    if i.split('_')[0] == 'us':

                        new_skill = UserGeneratedSkills()

                        new_skill.skill_id = len(UserGeneratedSkills.objects.all()) + 1
                        new_skill.name = i.split('_')[1]

                        new_skill.save()

                        new_candidate_skills = CandidateSkills()

                        new_candidate_skills.user_id = new_candidate

                        new_candidate_skills.skill_id = 'us_' + str(new_skill.skill_id)

                        new_candidate_skills.save()

                    else:

                        new_candidate_skills = CandidateSkills()

                        new_candidate_skills.user_id = new_candidate

                        new_candidate_skills.skill_id = i

                        new_candidate_skills.save()

            return 1

        if self.post_data['page'] == '1':

            if CandidateFields.objects.filter(user_id__username=self.request.user.username).exists():

                if 'candidate_resume' not in self.request.FILES:
                    return 'resume_not_found_error'

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

                # below is code to upload resume

                candidate_resume = self.request.FILES['candidate_resume']

                fs = FileSystemStorage(location='static/resumes/')

                filename = fs.save(candidate_resume.name, candidate_resume)

                uploaded_file_url = fs.url(filename)

                old_candidate.resume_file_name = uploaded_file_url

                old_candidate.current_location_id = self.post_data['current_city']

                old_candidate.save()

                preferred_cities = self.post_data.getlist('open_to_city[]')

                if CandidateInterestedCities.objects.filter(user_id__user_id__username=self.request.user.username).exists():

                    CandidateInterestedCities.objects.filter(user_id__user_id__username=self.request.user.username).delete()

                for p in preferred_cities:

                    new_city = CandidateInterestedCities()

                    new_city.user_id = old_candidate
                    new_city.interested_city_value = p

                    new_city.save()

                return 2

            else:

                return "send_user_page_1"

        if self.post_data['page'] == '2':

            if CandidateFields.objects.filter(user_id__username=self.request.user.username).exists():

                if 'event_subscribe' not in self.post_data:

                    return 'event_subscribe_not_found_error'

                if 'newsletter_subscribe' not in self.post_data:

                    return 'newsletter_subscribe_not_found_error'

                old_candidate = CandidateFields.objects.get(user_id__username=self.request.user.username)

                if self.post_data['event_subscribe'] == 'yes':

                    old_candidate.event_subscribe = True

                if self.post_data['event_subscribe'] == 'no':

                    old_candidate.event_subscribe = False

                if self.post_data['newsletter_subscribe'] == 'yes':

                    old_candidate.newsletter_subscribe = True

                if self.post_data['newsletter_subscribe'] == 'no':

                    old_candidate.newsletter_subscribe = False

                old_candidate.save()

                return 3

            else:

                return "send_user_page_1"

