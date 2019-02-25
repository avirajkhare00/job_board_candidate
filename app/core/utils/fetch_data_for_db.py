from app.core.utils.fetch_job_functions import FetchJobFunctions
from app.core.utils.fetch_primary_skills import FetchPrimarySkills
from app.core.utils.fetch_secondary_skills import FetchSecondarySkills
from app.core.utils.fetch_primary_secondary_skills import FetchPrimarySecondarySkills
from app.core.utils.fetch_industry_type import FetchIndustryType
from app.core.utils.fetch_degrees import FetchCollegeDegree
from app.core.utils.fetch_specializations import FetchCollegeSpecialization
from app.core.utils.fetch_cities_name_india import FetchCitiesNameIndia


class FetchDataForDb:

    def fetch_data(self):

        FetchJobFunctions().fetch_data()

        #FetchPrimarySkills().fetch_skills()

        #FetchSecondarySkills().fetch_data()

        FetchPrimarySecondarySkills().push_to_db()# this function is equivalent to both above functions.

        FetchIndustryType().fetch_data()

        FetchCollegeDegree().fetch_data()

        FetchCollegeSpecialization().fetch_data()

        FetchCitiesNameIndia().fetch_data()

        return 1
