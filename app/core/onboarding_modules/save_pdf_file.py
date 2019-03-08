# this module stores pdf file and gives out pdf file name
# file name will be unique for each and every Candidate

from django.core.files.storage import FileSystemStorage
from app.models import CandidateFields
from secrets import choice
import string

# ''.join([choice(string.ascii_uppercase + string.digits) for _ in range(N)])

class SavePDFFile:

    def __init__(self, file_object):

        #there is very high probability that first time string will be unique
        self.unique_string = ''.join([choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(6)]) + '.pdf'
        self.condition = True
        self.file_object = file_object

    def save_file(self):

        while self.condition == True:
        
            if CandidateFields.objects.filter(resume_file_name=self.unique_string).exists():

                self.unique_string = ''.join([choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(10)]) + '.pdf'

            else:

                self.condition = False

        candidate_resume = self.file_object

        fs = FileSystemStorage(location='static/resumes/')

        filename = fs.save(self.unique_string, candidate_resume)

        uploaded_file_url = fs.url(filename)

        return uploaded_file_url
