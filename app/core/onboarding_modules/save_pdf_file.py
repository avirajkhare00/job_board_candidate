# this module stores pdf file and gives out pdf file name
# file name will be unique for each and every Candidate

from django.core.files.storage import FileSystemStorage
from app.models import CandidateFields
import random
import string

# ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])

class SavePDFFile:

    def __init__(self, file_object):

        #there is very high probability that first time string will be unique
        self.unique_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)]) + '.pdf'
        self.condition = True
        self.file_object = file_object

    def save_file(self):

        while self.condition == True:
        
            if CandidateFields.objects.filter(resume_file_name=self.unique_string).exists():

                self.unique_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)]) + '.pdf'

            else:

                self.condition = False

        candidate_resume = self.file_object

        fs = FileSystemStorage(location='static/resumes/')

        filename = fs.save(self.unique_string, candidate_resume)

        uploaded_file_url = fs.url(filename)

        return uploaded_file_url
