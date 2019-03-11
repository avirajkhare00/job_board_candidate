from django.shortcuts import render, HttpResponse, redirect
from common_app.models import PasswordUserMapping
from django.contrib.auth.models import User

# Create your views here.

def forget_password_view(request):

    if request.method == 'GET':

        return render(request, 'html3/forget_password.html')

    if request.method == 'POST':

        print(request.POST)

        if User.objects.filter(email=request.POST['candidate_email']).exists():

            print('user_exists')
            
            return redirect('../forget_password/?status=correct_email')

        else:

            print('user_does_not_exists')

            return redirect('../forget_password/?status=wrong_email')


def forget_password_success_page_view(request):

    if request.method == 'GET':

        if 'success_type' in request.GET:

            if request.GET['success_type'] == 'success':

                return render(request, 'html3/password_success.html', {
                    'success': True
                })

            if request.GET['success_type'] == 'invalid_email':

                return render(request, 'html3/password_success.html'), {
                    'success': False
                }

        else:

            return redirect('../forget_password/')

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

                return redirect('../forget_password/')

        else:

            return redirect('../forget_password/')