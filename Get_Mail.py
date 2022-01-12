import Mail


class Get_Mail():

    def __init__(self):

        self.Mail = Mail.Mail()




    def set_mail(self, mail_addres, password):

        self.Mail.gmail_user = mail_addres
        self.Mail.gmail_password = password


        self.Mail.log_in()
        self.Mail.get_twitch_mail()

