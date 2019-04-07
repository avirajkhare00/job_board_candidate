from app.models import CandidateFields, CandidateSkills, UserGeneratedSkills


class StoreUserOnboardingDataPage1:

    def __init__(self, request):

        self.request = request
        self.post_data = self.request.POST

    def store_data(self):

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

                if i.split('_')[0] == 'usd':
                    new_skill = UserGeneratedSkills()

                    new_skill.skill_id = len(UserGeneratedSkills.objects.all()) + 1
                    new_skill.name = i.split('_')[1]

                    new_skill.save()

                    new_candidate_skills = CandidateSkills()

                    new_candidate_skills.user_id = old_candidate

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

                if i.split('_')[0] == 'usd':

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

            new_candidate.onboarding_step_1_completed = True

            new_candidate.save()

        return 1
