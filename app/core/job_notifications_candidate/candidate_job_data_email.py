from app.core.filter_jobs.filter_candidate_jobs import FilterCandidateJobs
from app.core.data_components.get_job_by_id import GetJobById


class CandidateJobDataEmail:

    def __init__(self, username):

        self.username = username
        self.job_data_array = []

    def get_data_array(self):

        for filtered_jobs in FilterCandidateJobs(self.username).filter_jobs():

            for filtered_job_id in filtered_jobs:

                job_object = GetJobById(filtered_job_id).get_data()

                self.job_data_array.append({
                    "job_name": job_object['job_name'],
                    "company_name": job_object['company_name'],
                    "job_slug": job_object['job_slug']
                })

        return self.job_data_array
