from app.models import CandidateFields
from app.core.mail_modules.fire_flow import FireFlow


class StoreOnboardingUserDataPage3:

    def __init__(self, request):

        self.request = request
        self.post_data = self.request.POST

    def store_data(self):

        if CandidateFields.objects.filter(user_id__username=self.request.user.username).exists():

            if 'event_subscribe' not in self.post_data:
                return 'event_subscribe_not_found_error'

            if 'newsletter_subscribe' not in self.post_data:
                return 'newsletter_subscribe_not_found_error'

            old_candidate = CandidateFields.objects.get(user_id__username=self.request.user.username)

            if self.post_data['event_subscribe'] == 'yes':
                old_candidate.event_subscribe = True

            if self.post_data['event_subscribe'] == 'no':
                old_candidate.event_subscribe = False

            if self.post_data['newsletter_subscribe'] == 'yes':
                old_candidate.newsletter_subscribe = True

            if self.post_data['newsletter_subscribe'] == 'no':
                old_candidate.newsletter_subscribe = False

            # create a new BooleanField to check weather user filled details first time
            # if user.is_first_time == True: send email and turn off condition to false
            if old_candidate.welcome_email_sent == False:

                # check weather user signed condition for newsletter and event
                # by default we will send third flow email
                if self.post_data['newsletter_subscribe'] == 'yes':
                    pass
                    # FireFlow(old_candidate.user_id.first_name, old_candidate.user_id.email, 2).select_flow_and_fire()

                if self.post_data['event_subscribe'] == 'yes':
                    pass
                    # FireFlow(old_candidate.user_id.first_name, old_candidate.user_id.email, 3).select_flow_and_fire()

                # by default for flow_id: 4
                # FireFlow(old_candidate.user_id.first_name, old_candidate.user_id.email, 4).select_flow_and_fire()

                FireFlow(old_candidate.user_id.first_name, old_candidate.user_id.email, 1).select_flow_and_fire()

                old_candidate.welcome_email_sent = True

            old_candidate.onboarding_step_3_completed = True

            old_candidate.save()

            return 3

        else:

            return "send_user_page_1"
