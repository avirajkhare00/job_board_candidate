from django.contrib.auth.models import User
from app.core.mail_modules.fire_flow import FireFlow
import re

class ValidateSignup:

    def __init__(self, post_data):

        self.post_data = post_data

    def validate_it(self):

        if 'candidate_name' not in self.post_data:

            return 'no_name'

        if 'candidate_email' not in self.post_data:

            return 'no_email'

        if 'candidate_password' not in self.post_data:

            return 'no_password'

        if 'candidate_username' not in self.post_data:

            return 'no_username'

        if User.objects.filter(username=self.post_data['candidate_username']).exists():

            return 'username_exists'

        if len(self.post_data['candidate_username']) <= 3:

            return 'username_short'

        if User.objects.filter(email=self.post_data['candidate_email']):

            return 'email_exists'

        if len(self.post_data['candidate_password']) < 4:

            return 'password_short'

        if len(self.post_data['candidate_name'].lstrip().rstrip().split(' ')) <= 1:

            return 'no_full_name'

        if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.post_data['candidate_email']) is None:

            return 'invalid_email'

        if re.match("^[a-zA-Z0-9_.-]+$", self.post_data['candidate_username']) is None:

            return 'invalid_username'

        else:

            # create new user
            # authenticate user
            # redirect user to onboarding page
            new_user = User()

            new_user.first_name = self.post_data['candidate_name'].lstrip().rstrip().split(' ')[0]
            new_user.last_name = self.post_data['candidate_name'].lstrip().rstrip().split(' ')[1:]
            new_user.email = self.post_data['candidate_email']
            new_user.username = self.post_data['candidate_username']
            new_user.set_password(self.post_data['candidate_password'])

            new_user.save()

            #inserting fire_flow to send transactional email
            FireFlow(new_user.first_name, new_user.email, 1).select_flow_and_fire()

            return 'ok'
