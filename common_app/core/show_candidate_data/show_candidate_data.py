from app.models import CandidateFields, CandidateSkills, CandidateInterestedCities
from app.models import PrimarySkills, SecondarySkills, UserGeneratedSkills, JobName


class ShowCandidateData:

    def __init__(self):

        self.data_object = {
            "status": "ok",
            "candidate_data": []
        }

    def convert_skill_object_to_list(self, user_id):

        skill_list = []

        for candidate_skill in CandidateSkills.objects.filter(user_id__user_id__username=user_id):

            if candidate_skill.skill_id.split('_')[0] == 'ps':

                skill_list.append(PrimarySkills.objects.get(primary_skill_id=candidate_skill.skill_id.split('_')[1]).name)

            if candidate_skill.skill_id.split('_')[0] == 'ss':

                skill_list.append(SecondarySkills.objects.get(secondary_skill_id=candidate_skill.skill_id.split('_')[1]).name)

            if candidate_skill.skill_id.split('_')[0] == 'us':

                skill_list.append(UserGeneratedSkills.objects.get(skill_id=candidate_skill.skill_id.split('_')[1]).name)

        return skill_list

    def fetch_data_from_db(self):

        for candidate in CandidateFields.objects.all():

            self.data_object['candidate_data'].append(
                {
                    "first_name": candidate.user_id.first_name,
                    "email": candidate.user_id.email,
                    "job_name": JobName.objects.get(job_name_id=candidate.candidate_job_id).job_name,
                    "candidate_skills": ', '.join(self.convert_skill_object_to_list(candidate.user_id))
                }
            )

        return self.data_object
