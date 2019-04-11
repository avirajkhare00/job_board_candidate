from app.core.job_notifications_candidate.candidate_job_data_email import CandidateJobDataEmail
from app.core.filter_candidates.filter_candidates import FilterCandidates


class JobNotificationsCandidate:

    def __init__(self, condition):

        self.condition = condition
        self.final_json_data = {
            "status": "ok",
            "candidate_data": []
        }

    def send_data(self):

        if self.condition == 'test':

            for candidate in FilterCandidates('test').get_data():

                self.final_json_data['candidate_data'].append(
                    {
                        "email": candidate['email'],
                        "first_name": candidate['first_name'],
                        "jobs_data": CandidateJobDataEmail(candidate['username']).get_data_array()
                    }
                )

        if self.condition == 'prod':

            for candidate in FilterCandidates('all').get_data():

                self.final_json_data['candidate_data'].append(
                    {
                        "email": candidate['email'],
                        "first_name": candidate['first_name'],
                        "jobs_data": CandidateJobDataEmail(candidate['username']).get_data_array()
                    }
                )
