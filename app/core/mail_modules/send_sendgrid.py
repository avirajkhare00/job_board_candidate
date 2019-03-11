import sendgrid
import os
from sendgrid.helpers.mail import *

class SendMailSendGrid:

    def __init__(self, to_email, subject, content):

        self.to_email = to_email
        self.subject = subject
        self.content = content

        self.API_KEY = "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"

    def send_it(self):

        sg = sendgrid.SendGridAPIClient(apikey=self.API_KEY)
        from_email = Email("noreply@hellomeets.com")
        to_email = Email(self.to_email)
        subject = self.subject
        content = Content("text/html", self.content)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        # print(response.body)
        # print(response.headers)