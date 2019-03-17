from app2.models import JobPost, JobSkills
from app.models import UserGeneratedSkills, IndianCityName


class UpdateJobById:

    def __init__(self, post_data, job_id):

        self.post_data = post_data
        self.job_id = job_id

    def update_job(self):

        selected_job = JobPost.objects.get(id=self.job_id)

        # selected_job.job_location_id = self.post_data['job_location_id']
        selected_job.job_description = self.post_data['job_content']

        if '_' in self.post_data['job_location_id']:

            if self.post_data['job_location_id'].split('_')[0] == 'ucity':

                new_city = IndianCityName()

                new_city.city_name = self.post_data['job_location_id'].split('_')[1].capitalize()
                new_city.city_value = self.post_data['job_location_id'].split('_')[1]

                new_city.save()

                selected_job.job_location_id = self.post_data['job_location_id'].split('_')[1].capitalize()

            else:

                selected_job.job_location_id = self.post_data['job_location_id']

        else:

            selected_job.job_location_id = self.post_data['job_location_id']

        selected_job.save()

        job_skills = self.post_data.getlist('skills[]')

        print(job_skills)

        JobSkills.objects.filter(job_id=selected_job).delete()

        for job_skill in job_skills:

            # TODO rewrite better algorithm to update skills both in candidate onboarding side and update job side

            if job_skill.split('_')[0] == 'uss':

                new_skill = UserGeneratedSkills()

                new_skill.skill_id = len(UserGeneratedSkills.objects.all()) + 1
                new_skill.name = job_skill.split('_')[1]

                new_skill.save()

                new_new_skill = JobSkills()

                new_new_skill.job_id = selected_job
                new_new_skill.job_skill_id = 'us_' + str(new_skill.skill_id)

                new_new_skill.save()

            else:

                job_skill_skill = JobSkills()

                job_skill_skill.job_id = selected_job
                job_skill_skill.job_skill_id = job_skill

                job_skill_skill.save()

        return 'ok'
