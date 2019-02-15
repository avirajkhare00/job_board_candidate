import json
from app.models import CollegeDegrees

class FetchCollegeDegree:

    def __init__(self):

        self.raw_data = '{"objects": [{"resource_uri": "/api/v1/degrees/1", "id": 1, "name_nopunc": "ba", "name": "BA"}, {"resource_uri": "/api/v1/degrees/2", "id": 2, "name_nopunc": "barch", "name": "BArch"}, {"resource_uri": "/api/v1/degrees/3", "id": 3, "name_nopunc": "bba", "name": "BBA"}, {"resource_uri": "/api/v1/degrees/4", "id": 4, "name_nopunc": "bca", "name": "BCA"}, {"resource_uri": "/api/v1/degrees/5", "id": 5, "name_nopunc": "bcom", "name": "BCom"}, {"resource_uri": "/api/v1/degrees/6", "id": 6, "name_nopunc": "bdes", "name": "BDes"}, {"resource_uri": "/api/v1/degrees/7", "id": 7, "name_nopunc": "bsc", "name": "BSc"}, {"resource_uri": "/api/v1/degrees/8", "id": 8, "name_nopunc": "btechbe", "name": "BTech / BE"}, {"resource_uri": "/api/v1/degrees/9", "id": 9, "name_nopunc": "ca", "name": "CA"}, {"resource_uri": "/api/v1/degrees/10", "id": 10, "name_nopunc": "cs", "name": "CS"}, {"resource_uri": "/api/v1/degrees/11", "id": 11, "name_nopunc": "diploma", "name": "Diploma"}, {"resource_uri": "/api/v1/degrees/12", "id": 12, "name_nopunc": "llb", "name": "LLB"}, {"resource_uri": "/api/v1/degrees/13", "id": 13, "name_nopunc": "llm", "name": "LLM"}, {"resource_uri": "/api/v1/degrees/14", "id": 14, "name_nopunc": "ma", "name": "MA"}, {"resource_uri": "/api/v1/degrees/15", "id": 15, "name_nopunc": "march", "name": "MArch"}, {"resource_uri": "/api/v1/degrees/16", "id": 16, "name_nopunc": "mbapgdm", "name": "MBA / PGDM"}, {"resource_uri": "/api/v1/degrees/17", "id": 17, "name_nopunc": "mbbs", "name": "MBBS"}, {"resource_uri": "/api/v1/degrees/18", "id": 18, "name_nopunc": "mca", "name": "MCA"}, {"resource_uri": "/api/v1/degrees/19", "id": 19, "name_nopunc": "mcom", "name": "MCom"}, {"resource_uri": "/api/v1/degrees/20", "id": 20, "name_nopunc": "mdes", "name": "MDes"}, {"resource_uri": "/api/v1/degrees/21", "id": 21, "name_nopunc": "mtechmsc", "name": "MTech / MSc"}, {"resource_uri": "/api/v1/degrees/22", "id": 22, "name_nopunc": "other", "name": "Other"}, {"resource_uri": "/api/v1/degrees/23", "id": 23, "name_nopunc": "phd", "name": "PhD"}, {"resource_uri": "/api/v1/degrees/24", "id": 24, "name_nopunc": "bpharma", "name": "BPharma"}, {"resource_uri": "/api/v1/degrees/25", "id": 25, "name_nopunc": "mpharma", "name": "MPharma"}], "meta": {"total_count": 25, "previous": null, "limit": 1000, "offset": 0, "next": null}}'
        self.json_data = json.loads(self.raw_data)['objects']

    def fetch_data(self):

        for degree in self.json_data:

            new_degree = CollegeDegrees()

            new_degree.name = degree['name']
            new_degree.college_degree_id = int(degree['id'])
            new_degree.slug_name = degree['name_nopunc']

            new_degree.save()
