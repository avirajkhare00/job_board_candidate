from app2.models import JobPost, HomeRecruiter, JobsByRecruiter


class FetchJobIds:

    def __init__(self, username):

        self.username = username
        self.job_id_data = {
            'status': False,
            'job_ids': []
        }

    def fetch_ids(self):

        if JobsByRecruiter.objects.filter(recruiter_id__recruiter_id__username=self.username).exists():

            self.job_id_data['status'] = True

            for job_id in JobsByRecruiter.objects.filter(recruiter_id__recruiter_id__username=self.username):

                self.job_id_data['job_ids'].append(job_id.job_id)

            return self.job_id_data

        else:

            self.job_id_data['status'] = False
            return self.job_id_data
