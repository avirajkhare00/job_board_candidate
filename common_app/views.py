from django.shortcuts import render, HttpResponse, redirect
from common_app.models import PasswordUserMapping
from common_app.core.forget_password_modules.forget_password import ForgetPassword
from common_app.core.forget_password_modules.set_new_password import SetNewPassword

# Create your views here.


def forget_password_view(request):

    if request.method == 'GET':

        return render(request, 'html3/forget_password.html')

    if request.method == 'POST':

        # call a method here
        ForgetPassword(request.POST['candidate_email']).check_and_send_mail()
            
        return redirect('../email_sent/')


def forget_password_success_page_view(request):

    if request.method == 'GET':

        return render(request, 'html3/password_success.html')

    if request.method == 'POST':

        return HttpResponse(401)


def set_new_password_view(request):

    if request.method == 'GET':

        if 's' in request.GET:

            if PasswordUserMapping.objects.filter(random_string=request.GET['s']).exists():

                return render(request, 'html3/set_new_password.html', {
                    's': request.GET['s']
                })

            else:

                return HttpResponse('invalid link. Please request new password.')

        else:

            return HttpResponse('invalid link. please request new password.')

    if request.method == 'POST':

        if 'random_string' not in request.POST:

            return HttpResponse(401)

        elif 'new_password' not in request.POST:

            return HttpResponse(401)

        else:

            reset_status = SetNewPassword(request.POST['random_string'], request.POST['new_password']).verify_string_and_set_password()

            if reset_status == 0:

                return render(request, 'html3/new_password_success.html')

            if reset_status == -1:

                return HttpResponse(401)
