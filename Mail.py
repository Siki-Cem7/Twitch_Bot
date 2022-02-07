import smtplib
import email
import imaplib
from bs4 import BeautifulSoup




class Mail():


    def __init__(self):

        self.gmail_user = None
        self.gmail_password = None




    def set_name(self):



        self.mail = {

        "from"   :f"{self.gmail_user}"

        }




    def log_in(self):



        self.server = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        self.server.login(user=self.gmail_user, password=self.gmail_password)





    def get_twitch_mail(self):

        self.server.select("inbox")

        result, data = self.server.search(None, "ALL")


        ids = data[0]  # data is a list.
        id_list = ids.split()  # ids is a space separated string
        latest_email_id = id_list[-1]  # get the latest


        result, data = self.server.fetch(latest_email_id, "(RFC822)")  # fetch the email body (RFC822) for the given ID





        raw_email = data[0][1]  # here's the body, which is raw text of the whole email
        # including headers and alternate payloads


        raw_email = str(raw_email)

        html = BeautifulSoup(raw_email, "html.parser")
        self.code = html.find(class_="3Dheader-message-code")
        print(self.code)
        self.code = self.code.get_text()


        for char in self.code:

            if(char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9"):
                None
            else:
                self.code = self.code.replace(char, "", 1)











    def send_mail(self):


        try:
            self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            self.server.ehlo()
            self.server.login(self.gmail_user, self.gmail_password)

            self.message = 'Subject: {}\n\n{}'.format(self.mail["subject"], self.mail["body"])
            self.server.sendmail(from_addr=self.mail["from"],to_addrs=self.mail["to"],msg=self.message)

        except:
            print('Something went wrong...')



if __name__ == "__main__":

    mail = Mail()
    mail.log_in()
    mail.get_twitch_mail()
