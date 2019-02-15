from app.models import PrimarySkills, SecondarySkills
from django.core import serializers

class FetchSuggestedSkills:

    def __init__(self, query_data):

        self.query_data = query_data
        self.fetched_data = {}

    def fetch_data(self):

        self.fetched_data['status'] = 'ok'

        self.fetched_data['data'] = serializers.serialize(
            'json',
            PrimarySkills.objects.filter(associated_to_job__job_name_id=int(self.query_data['job_id'])),
            fields=('primary_skill_id','name')
        )

        return self.fetched_data
