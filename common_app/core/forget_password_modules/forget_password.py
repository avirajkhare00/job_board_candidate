from django.contrib.auth.models import User
from common_app.models import PasswordUserMapping
from app.core.mail_modules.fire_flow import FireFlow
import random
import string


class ForgetPassword:

    def __init__(self, email):

        self.email = email
        self.property_dict = {
            'property_dict': ''
        }

    def check_and_send_mail(self):

        if User.objects.filter(email=self.email).exists():

            if PasswordUserMapping.objects.filter(user_id__email=self.email).exists():

                PasswordUserMapping.objects.filter(user_id__email=self.email).delete()

            user = User.objects.get(email=self.email)

            new_password_string = PasswordUserMapping()
            new_password_string.user_id = user
            new_password_string.random_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(128)])

            new_password_string.save()

            self.property_dict['password_reset_link'] = new_password_string.random_string

            FireFlow(user.first_name, user.email, 6).select_util_flow_and_fire(self.property_dict)

            return

        else:

            return
