from app.core.mail_modules.send_sendgrid import SendMailSendGrid


class FireFlow:

    def __init__(self, first_name, email, flow_id):

        self.first_name = first_name
        self.email = email
        self.flow_id = flow_id

    def select_flow_and_fire(self):

        if self.flow_id == 1:

            SendMailSendGrid(
                self.email,
                "Welcome to HelloMeets Job Board.",
                "Hello <b>" + self.first_name + "</b><br />" +
                "Welcome on board.<br /><br />"
                "<b>Important Tip:</b> Upload your resume to make you easily searchable for companies.<br /><br />" +
                "How this Job Board works?<br />" +
                "<ol>" +
                    "<li>Once you sign in, you will be able to see all jobs based on your skills.</li>" +
                    "<li>Apply for the job you are interested in.</li>" +
                    "<li>If the company is interested in your profile, they will contact you.</li>" +
                    "<li>You will also receive weekly job updates that match your preferences.</li>" +
                "</ol><br />" +
                "Thanks for being a part of the community and considering HelloMeets to find your next job.<br /><br />"
                "Best,<br />" +
                "<b>HelloMeets</b>"
            ).send_it()

        if self.flow_id == 2:

            SendMailSendGrid(
                self.email,
                "Thank you for subscribing HelloMeets Newsletter.",
                "Hello <b>" + self.first_name + "</b><br />You will keep on receiving upcoming newsletter from our community."
            ).send_it()

        if self.flow_id == 3:
            
            SendMailSendGrid(
                self.email,
                "Thank you for subscribing HelloMeets Events.",
                "Hello <b>" + self.first_name + "</b><br />Now you’ll receive notifications about events in your city."
            ).send_it()

        if self.flow_id == 4:

            SendMailSendGrid(
                self.email,
                "Thank you for completing your HelloMeets JobBoard Profile.",
                "Hello <b>" + self.first_name + "</b><br />You have successfully completed your HelloMeets Job Board Profile.<br />You will receive weekly job alerts based on your preferences."
            ).send_it()

        if self.flow_id == 5:

            SendMailSendGrid(
                self.email,
                "Welcome to the HelloMeets Job Board",
                "Hello <b>" + self.first_name + "</b><br />" +
                "Thanks for being a part of the community and considering HelloMeets as one of your hiring channels.<br /><br />" +
                "How this works?<br />" +
                "<ol>" +
                    "<li>Once a candidate applies to your job opening, you will receive an email along with their resume. Please feel free to contact them.</li>" +
                    "<li>You will receive weekly job updates that match your job opening.</li>" +
                "</ol><br /><br />" +
                "Best,<br />" +
                "<b>HelloMeets</b>"

            ).send_it()

        if self.flow_id == 7:

            SendMailSendGrid(
                self.email,
                "HelloMeets JobBoard - Password Changed",
                "Hello <b>" + self.first_name + "</b><br />Your password is changed successfully."
            ).send_it()

    def select_util_flow_and_fire(self, property_dict):

        if self.flow_id == 6:

            SendMailSendGrid(
                self.email,
                "HelloMeets JobBoard Forget Password",
                "Hello <b>" + self.first_name + "</b><br />Click on this link to reset your password: <a href='https://jobboard.hellomeets.com/new_password/?s=" + property_dict['password_reset_link'] + "'>PASSWORD RESET LINK</a><br />If you did not request it, please ignore this mail."
            ).send_it()

        if self.flow_id == 8:

            SendMailSendGrid(
                self.email,
                "HelloMeets JobBoard - New Job Posted",
                "Hello <b>" + self.first_name + "</b><br />You have posted a new job.<br /><a href='https://jobboard.hellomeets.com/job/" + property_dict['job_slug'] + "'>view job</a>"
            ).send_it()

        if self.flow_id == 9:

            # TODO finish it in the end.

            pass

        if self.flow_id == 10:

            SendMailSendGrid(
                self.email,
                "HelloMeets JobBoard - New Candidate Application",
                "Hello <b>" +
                self.first_name +
                "</b><br />" +
                "A new candidate has applied for the job opening you posted. <br />" +
                "Job Name: <b>" + property_dict['job_name'] + "</b><br />" +
                "Job Link: <a href='https://jobboard.hellomeets.com/job/" + property_dict['job_slug'] + "'><b>view job</b></a><br />" +
                "Candidate Name: <b>" + property_dict['candidate_name'] + "</b><br />" +
                "Candidate Email: <b>" + property_dict['candidate_email'] + "</b><br />" +
                "Resume Link: <b><a href='https://jobboard.hellomeets.com/static/resumes/" + property_dict['candidate_resume_link'] + "'>click here to view resume</a></b><br />" +
                "Best, <br />" +
                "<b>HelloMeets</b>"
            ).send_it()
