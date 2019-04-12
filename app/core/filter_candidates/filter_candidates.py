from app.models import CandidateFields


class FilterCandidates:

    def __init__(self, select_type):

        self.select_type = select_type
        self.candidate_data = []

    def get_data(self):

        if self.select_type == 'all':

            for candidate in CandidateFields.objects.all():

                self.candidate_data.append(
                    {
                        "first_name": candidate.user_id.first_name,
                        "email": candidate.user_id.email,
                        "username": candidate.user_id.username
                    }
                )

            return self.candidate_data

        else:

            test_candidate = CandidateFields.objects.get(user_id__email='systems@hellomeets.com')

            self.candidate_data.append(
                {
                    "first_name": test_candidate.user_id.first_name,
                    "email": test_candidate.user_id.email,
                    "username": test_candidate.user_id.username
                }
            )

            return self.candidate_data
