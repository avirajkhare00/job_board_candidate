from app2.models import JobApplicants, JobPost


class JobApplicantLogin:

    def __init__(self, email, job_id):

        self.email = email
        self.job_id = job_id

    def store_job_applicant(self):

        if JobApplicants.objects.filter(applicant_email=self.email).exists():

            return 'already_applied'

        else:

            new_applicant = JobApplicants()

            new_applicant.applicant_email = self.email
            new_applicant.job_id = JobPost.objects.get(id=self.job_id)

            new_applicant.save()

            return 'ok'
