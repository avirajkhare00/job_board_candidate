from django.contrib.auth.models import User
from app.models import CandidateFields
from app2.models import JobApplicants, JobPost
from app.core.mail_modules.fire_flow import FireFlow


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

            # one time mail will go here.
            FireFlow(
                new_applicant.job_id.job_id.company_id.first_name,
                new_applicant.job_id.job_id.company_id.email,
                10
            ).select_util_flow_and_fire({
                "job_name": new_applicant.job_id.job_name,
                "job_slug": new_applicant.job_id.job_slug,
                "candidate_name": User.objects.get(email=new_applicant.applicant_email).first_name, # TODO make logic to remove [] from last name
                "candidate_email": self.email,
                "candidate_resume_link": CandidateFields.objects.get(user_id__email=self.email).resume_file_name
            })

            return 'ok'
