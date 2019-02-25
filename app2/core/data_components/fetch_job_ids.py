from app2.models import JobPost


class FetchJobIds:

    def __init__(self, username):

        self.username = username
        self.job_id_data = {
            'status': False,
            'job_ids': []
        }

    def fetch_ids(self):

        if JobPost.objects.filter(job_id__company_id__username=self.username).exists():

            self.job_id_data['status'] = True

            for job in JobPost.objects.filter(job_id__company_id__username=self.username):

                self.job_id_data['job_ids'].append(job.id)

            return self.job_id_data

        else:

            self.job_id_data['status'] = False
            return self.job_id_data
