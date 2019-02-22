from app2.models import JobPost, JobSkills, CompanyDetails


class StoreNewJob:

    def __init__(self, post_data, username):

        self.post_data = post_data
        self.username = username

    def store_data(self):

        if 'job_name' not in self.post_data:

            return 'job_name_not_found_error'

        if 'job_category_id' not in self.post_data:

            return 'job_category_not_found_error'

        if 'job_location_id' not in self.post_data:

            return 'job_location_not_found_error'

        if 'skills[]' not in self.post_data:

            return 'skills_not_found_error'

        if 'job_content' not in self.post_data:

            return 'job_content_not_found_error'

        company_id = CompanyDetails.objects.get(company_id__username=self.username)

        new_job = JobPost()

        new_job.job_id = company_id
        new_job.job_name = self.post_data['job_name']
        new_job.job_slug = company_id.company_name.lower().replace(' ','-') + '-' + self.post_data['job_name'].lower().replace(' ','-')
        new_job.job_name_id = int(self.post_data['job_category_id'])
        new_job.job_location_id = self.post_data['job_location_id']
        new_job.job_description = self.post_data['job_content']

        if self.post_data['is_draft'] == 'false':

            new_job.is_draft = False

        if self.post_data['is_draft'] == 'true':

            new_job.is_draft = True

        new_job.save()

        for i in self.post_data.getlist('skills[]'):

            job_skill = JobSkills()

            job_skill.job_id = new_job
            job_skill.job_skill_id = i

            job_skill.save()

        return 'ok'
