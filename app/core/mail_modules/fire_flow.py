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
                "Welcome to HelloMeets JobBoard.",
                "Hello <b>" + self.first_name + "</b><br />Welcome to HelloMeets community. Please complete your profile."
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
                "Welcome to HelloMeets JobBoard",
                "Hello <b>" + self.first_name + "</b><br />Welcome on board.<br />Thanks for being a part of the community and considering HelloMeets as one of your hiring channels."
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
