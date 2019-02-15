from app.models import JobName, JobCategory
from django.core import serializers

class FetchJobCategories:

    def __init__(self):

        self.data = {
            'status': 'ok',
            'data': []
        }

    def fetch_categories(self):

        for j in JobCategory.objects.all().order_by('job_category_id'):

            self.data['data'].append({
                'job_category_name': j.name,
                'job_fields': serializers.serialize('json', JobName.objects.filter(job_category__job_category_id=j.job_category_id), fields=('job_name_id','job_name'))
            })

        return self.data
