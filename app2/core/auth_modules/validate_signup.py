from django.contrib.auth.models import User
from app2.models import CompanyDetails
from app.core.mail_modules.fire_flow import FireFlow
import re

class ValidateSignup:

    def __init__(self, post_data):

        self.post_data = post_data

    def validate_it(self):

        if 'employer_name' not in self.post_data:

            return 'no_name'

        if 'employer_email' not in self.post_data:

            return 'no_email'

        if 'employer_password' not in self.post_data:

            return 'no_password'

        if 'employer_username' not in self.post_data:

            return 'no_username'

        if 'company_name' not in self.post_data:

            return 'no_company_name'

        if len(self.post_data['company_name']) <= 3:

            return 'company_name_short'

        if User.objects.filter(username=self.post_data['employer_username']).exists():

            return 'username_exists'

        if len(self.post_data['employer_username']) <= 3:

            return 'username_short'

        if User.objects.filter(email=self.post_data['employer_email']):

            return 'email_exists'

        if len(self.post_data['employer_password']) < 4:

            return 'password_short'

        if len(self.post_data['employer_name'].lstrip().rstrip().split(' ')) <= 1:

            return 'no_full_name'

        if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.post_data['employer_email']) is None:

            return 'invalid_email'

        if re.match("^[a-zA-Z0-9_.-]+$", self.post_data['employer_username']) is None:

            return 'invalid username'

        else:

            # create new user
            # authenticate user
            # redirect user to onboarding page
            new_user = User()

            new_user.first_name = self.post_data['employer_name'].lstrip().rstrip().split(' ')[0]
            new_user.last_name = self.post_data['employer_name'].lstrip().rstrip().split(' ')[1:]
            new_user.email = self.post_data['employer_email']
            new_user.username = self.post_data['employer_username']
            new_user.set_password(self.post_data['employer_password'])

            new_user.save()

            new_company = CompanyDetails()

            new_company.company_id = new_user
            new_company.company_name = self.post_data['company_name']

            new_company.save()

            FireFlow(new_user.first_name, new_user.email, 5).select_flow_and_fire()

            return 'ok'
