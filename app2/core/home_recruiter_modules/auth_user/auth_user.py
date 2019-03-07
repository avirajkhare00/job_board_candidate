from app2.models import HomeRecruiter
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

class AuthUser:

    def __init__(self, request):

        self.request = request
        self.email = request.POST['employer_email']
        self.password = request.POST['employer_password']
        self.username = ''

    def check_and_auth_user(self):
        
        if User.objects.filter(email=self.email).exists():

            self.username = User.objects.get(email=self.email).username

            if HomeRecruiter.objects.filter(recruiter_id__username=self.username).exists() and HomeRecruiter.objects.get(recruiter_id__username=self.username).recruiter_activate:

                #authenticate the user and redirect user to new page

                user = authenticate(self.request, username=self.username, password=self.password)

                if user is not None:

                    login(self.request, user)

                    return "user_logged_in"

                else:

                    return "password_incorrect"

            else:

                return "permission_issue"

        else:

            return "user_not_exist"