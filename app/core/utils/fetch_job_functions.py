import requests
import json

from app.models import JobCategory, JobName

class FetchJobFunctions:

    def __init__(self):

        self.url = 'https://www.instahyre.com/api/v1/job_function'

    def fetch_data(self):

        r = requests.get(self.url).json()

        for job_function in r['objects']:

            print('job_name: ' + job_function['name'])
            print('category_name: ' + job_function['job_category']['name'])

            if JobCategory.objects.filter(job_category_id=int(job_function['job_category']['id'])).exists():

                existing_category = JobCategory.objects.get(job_category_id=int(job_function['job_category']['id']))

                new_job = JobName()

                new_job.job_category = existing_category
                new_job.job_name_id = job_function['id']
                new_job.job_name = job_function['name']
                new_job.job_name_slug = job_function['name'].lower().replace(' ', '-')

                new_job.save()

            else:

                new_category = JobCategory()
                new_category.job_category_id = int(job_function['job_category']['id'])
                new_category.name = job_function['job_category']['name']
                new_category.slug = job_function['job_category']['name'].lower().replace(' ', '-')

                new_category.save()

                new_job = JobName()

                new_job.job_category = new_category
                new_job.job_name_id = job_function['id']
                new_job.job_name = job_function['name']
                new_job.job_name_slug = job_function['name'].lower().replace(' ', '-')

                new_job.save()
