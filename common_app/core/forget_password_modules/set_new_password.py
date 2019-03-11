from django.contrib.auth.models import User
from common_app.models import PasswordUserMapping
from app.core.mail_modules.fire_flow import FireFlow


class SetNewPassword:

    def __init__(self, random_string, new_password):

        self.random_string = random_string
        self.new_password = new_password

    def verify_string_and_set_password(self):

        if PasswordUserMapping.objects.filter(random_string=self.random_string).exists():

            user = PasswordUserMapping.objects.get(random_string=self.random_string).user_id

            user.set_password(self.new_password)

            user.save()

            PasswordUserMapping.objects.get(random_string=self.random_string).delete()

            FireFlow(user.first_name, user.email, 7).select_flow_and_fire()

            return 0

        else:

            return -1
