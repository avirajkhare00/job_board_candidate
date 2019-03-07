from django.shortcuts import HttpResponse
import json
from app2.core.home_recruiter_modules.fetch_job_ids.fetch_job_ids import FetchJobIds


def fetch_job_id_recruiter(request):

    if request.method == 'GET':
    
        if request.user.is_authenticated:

            return HttpResponse(
                json.dumps({
                    'data': FetchJobIds(request.user.username).fetch_ids()
                }),
                content_type='application/json'
            )

        else:

            return HttpResponse(401)

    else:

        return HttpResponse(401)
