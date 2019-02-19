# we will iterate through each and every item of both objects in ascending order
# we will lowercase down and will push every name in a dict
# run these scripts in shell

from job_board_candidate.app.models import PrimarySkills, SecondarySkills

filter_list = []

for i in PrimarySkills.objects.all().order_by('-pk'):

    if i.name.lower() in filter_list:

        i.delete()

    else:

        filter_list.append(i.name.lower())

for j in SecondarySkills.objects.all().order_by('-pk'):

    if j.name.lower() in filter_list:

        j.delete()

    else:

        filter_list.append(j.name.lower())


['html','css','js','html']