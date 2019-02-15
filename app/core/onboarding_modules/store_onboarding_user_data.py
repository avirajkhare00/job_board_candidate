from app.models import CandidateFields, CandidateSkills, UserGeneratedSkills

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

            new_candidate = CandidateFields()

            new_candidate.user_id = self.request.user

            if self.post_data['candidate_status'] == 'professional':

                new_candidate.candidate_status = 1

            if self.post_data['candidate_status'] == 'student':

                new_candidate.candidate_status = 2

            new_candidate.save()

            for i in self.post_data.getlist('skills[]'):

                if i.split('_')[0] == 'us':

                    new_skill = UserGeneratedSkills()

                    new_skill.skill_id = len(UserGeneratedSkills.objects.all()) + 1
                    new_skill.name = i.split('_')[1]

                    new_skill.save()

                new_candidate_skills = CandidateSkills()

                new_candidate_skills.user_id = new_candidate

                new_candidate_skills.skill_id = i

                new_candidate_skills.save()

            return 1

        if self.post_data['page'] == '1':

            print(self.post_data)

            return 2
