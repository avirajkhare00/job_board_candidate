from app2.models import JobPost, JobSkills
from app.models import PrimarySkills, SecondarySkills, UserGeneratedSkills


class FetchJobById:

    def __init__(self, job_id):

        self.job_id = job_id
        self.job_data = {
            'status': '',
            'id': '',
            'job_name': '',
            'company_name': '',
            'job_location': '',
            'added_on': '',
            'job_slug': '',
            'skills': [],
            'is_active': True
        }

    def get_data(self):

        if JobPost.objects.filter(id=self.job_id).exists():

            job = JobPost.objects.get(id=self.job_id)

            skill_name = []

            for s in JobSkills.objects.filter(job_id=job):

                if s.job_skill_id.split('_')[0] == 'ps':
                    skill_obj = PrimarySkills.objects.get(primary_skill_id=int(s.job_skill_id.split('_')[1]))

                    skill_name.append({
                        'skill_name': skill_obj.name,
                        'id': skill_obj.primary_skill_id
                    })

                if s.job_skill_id.split('_')[0] == 'ss':
                    skill_obj = SecondarySkills.objects.get(secondary_skill_id=int(s.job_skill_id.split('_')[1]))

                    skill_name.append({
                        'skill_name': skill_obj.name,
                        'id': skill_obj.secondary_skill_id
                    })

                if s.job_skill_id.split('_')[0] == 'us':
                    skill_obj = UserGeneratedSkills.objects.get(skill_id=int(s.job_skill_id.split('_')[1]))

                    skill_name.append({
                        'skill_name': skill_obj.name,
                        'id': skill_obj.skill_id
                    })

            self.job_data['status'] = 'ok'
            self.job_data['id'] = job.id
            self.job_data['job_name'] = job.job_name
            self.job_data['company_name'] = job.job_id.company_name
            self.job_data['job_location'] = job.job_location_id
            self.job_data['added_on'] = str(job.added_on)
            self.job_data['job_slug'] = job.job_slug
            self.job_data['skills'] = skill_name
            self.job_data['is_active'] = job.is_active

            return self.job_data

        else:

            self.job_data['status'] = 'not_exist'

            return self.job_data
