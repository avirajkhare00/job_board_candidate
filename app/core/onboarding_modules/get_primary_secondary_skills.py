from app.models import PrimarySkills, SecondarySkills, UserGeneratedSkills
from django.core import serializers


class GetPrimarySecondarySkills:

    def __init__(self):

        self.data = {
            'status': 'ok',
            'fetched_data': {}
        }

    def get_data(self):

        self.data['fetched_data']['primary_skills'] = serializers.serialize(
            'json',
            PrimarySkills.objects.all(),
            fields=('primary_skill_id','name')
        )

        self.data['fetched_data']['secondary_skills'] = serializers.serialize(
            'json',
            SecondarySkills.objects.all(),
            fields=('secondary_skill_id','name')
        )

        self.data['fetched_data']['user_skills'] = serializers.serialize(
            'json',
            UserGeneratedSkills.objects.all(),
            fields=('skill_id','name')
        )

        return self.data
