from app2.models import CompanyDetails, JobPost, JobSkills, HomeRecruiter, JobsByRecruiter
from app.models import UserGeneratedSkills
from django.contrib.auth.models import User

class StoreRecruiterJobData:

    def __init__(self, request):

        self.post_data = request.POST
        self.username = request.user.username

    
    def store_data(self):

        if 'company_name' not in self.post_data:

            return 'no_company_name'

        if 'company_email' not in self.post_data:

            return 'no_company_email'

        if 'job_name' not in self.post_data:

            return 'no_job_name'

        if 'job_category_id' not in self.post_data:

            return 'no_job_category'

        if 'job_location_id' not in self.post_data:

            return 'no_job_location_id'

        if 'skills[]' not in self.post_data:

            return 'no_skills'

        if 'job_content' not in self.post_data:

            return 'no_job_content'

        else:

            if CompanyDetails.objects.filter(company_id__email=self.post_data['company_email']).exists():

                # use old company details and only create new job
                company_object = CompanyDetails.objects.get(company_id__email=self.post_data['company_email'])

            else:

                # creating new user and keeping email and username same
                new_user = User()

                new_user.username = self.post_data['company_email']
                new_user.email = self.post_data['company_email']
                new_user.set_password('some_random_password')

                new_user.save()

                company_object = CompanyDetails()

                company_object.company_id = new_user
                company_object.company_name = self.post_data['company_name']

                company_object.save()

            #since we will be creating new job, select new job object

            new_job = JobPost()

            new_job.job_id = company_object
            new_job.job_name = self.post_data['job_name']
            new_job.job_slug = company_object.company_name.lower().replace(' ','-') + '-' + self.post_data['job_name'].lower().replace(' ','-')
            new_job.job_name_id = int(self.post_data['job_category_id'])
            new_job.job_location_id = self.post_data['job_location_id']
            new_job.is_remote_friendly = False
            new_job.job_description = self.post_data['job_content']
            new_job.is_active = True

            new_job.save()

            for i in self.post_data.getlist('skills[]'):

                if i.split('_')[0] == 'us':

                    new_skill = UserGeneratedSkills()

                    new_skill.skill_id = len(UserGeneratedSkills.objects.all()) + 1
                    new_skill.name = i.split('_')[1]

                    new_skill.save()

                    new_new_skill = JobSkills()

                    new_new_skill.job_id = new_job
                    new_new_skill.job_skill_id = 'us_' + str(new_skill.skill_id)

                    new_new_skill.save()

                else:
                    
                    new_skill = JobSkills()
                    new_skill.job_id = new_job
                    new_skill.job_skill_id = i

                    new_skill.save()

            new_job_by_recruiter = JobsByRecruiter()

            new_job_by_recruiter.recruiter_id = HomeRecruiter.objects.get(recruiter_id__username=self.username)
            new_job_by_recruiter.job_id = new_job.id

            new_job_by_recruiter.save()

            return 'ok'

