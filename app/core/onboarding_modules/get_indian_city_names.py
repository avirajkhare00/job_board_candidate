from app.models import IndianCityName
from django.core import serializers


class GetIndianCityNames:

    def __init__(self):

        self.city_data = {
            'status' : 'ok',
            'data' : {}
        }

    def get_data(self):

        self.city_data['data'] = serializers.serialize(
            'json',
            IndianCityName.objects.all(),
            fields=('city_name','city_value')
        )

        return self.city_data
