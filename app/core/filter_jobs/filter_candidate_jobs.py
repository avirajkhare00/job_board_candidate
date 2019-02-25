from app2.models import JobPost, JobSkills
from app.models import CandidateSkills, CandidateFields

# we will filter jobs in two parameters
# 1. Job Function
# 2. Candidate Skills


class FilterCandidateJobs:

    def __init__(self, username):

        self.username = username
        self.unique_list = []

    def filter_jobs(self):

        current_position = CandidateFields.objects.get(user_id__username=self.username).candidate_job_id

        all_job_posts = JobPost.objects.filter(job_name_id=current_position, is_active=True)

        all_jobs_by_skills = []

        for skill in CandidateSkills.objects.filter(user_id__user_id__username=self.username):

            all_jobs_by_skills.append(JobSkills.objects.filter(job_skill_id=skill.skill_id, job_id__is_active=True))

        for job in all_job_posts:

            if job.id not in self.unique_list:

                self.unique_list.append(job.id)

        for all_jobs_skills_list in all_jobs_by_skills:

            for job in all_jobs_skills_list:

                if job.job_id.id not in self.unique_list:

                    self.unique_list.append(job.job_id.id)

        return self.unique_list
