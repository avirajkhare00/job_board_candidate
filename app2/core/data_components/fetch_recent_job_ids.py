from app2.models import JobPost


class FetchRecentJobIds:

    def __init__(self):

        self.job_id_data = {
            'status': False,
            'job_ids': []
        }

    def fetch_ids(self):

        self.job_id_data['status'] = True

        for job in JobPost.objects.filter(is_active=True).order_by('-id')[0:6]:

            self.job_id_data['job_ids'].append(job.id)

            return self.job_id_data

        else:

            self.job_id_data['status'] = False
            return self.job_id_data
