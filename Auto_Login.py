import sys
import time
import webbrowser
import requests
import subprocess
import keyboard
from pynput.keyboard import Key, Controller
import Get_Mail


class Twitch_log():


    def __init__(self):

        self.username = "username"
        self.password = "password"
        self.mail = "mail"
        self.password_mail = "password_mail"

        self.Get_Mail = Get_Mail.Get_Mail()


        self.url = "https://twitch.tv/login"


        self.accounts = {
            #"Main": {self.username: "sikicemjackson", self.password: "Internet07dasvierte", self.mail:"sommer.silvan3@gmail.com", self.password_mail:"Internet07dasvierte"},
            "1":{self.username:"dellasderaller", self.password:"IQwww349DF", self.mail:"siki.cemmii@gmail.com", self.password_mail:"Internet07dasvierte"},
            "2":{self.username:"markoderalleer", self.password:"Hee123dssaL6", self.mail:"bot.trackerreport@gmail.com", self.password_mail:"dasvierte"},
            "3":{self.username:"phillippderaller", self.password:"dfrSS349jfhg", self.mail:"wtdddfekomsichg@gmail.com", self.password_mail:"cdksks/()==(sdkf"}
        }







    def log(self, account):


        for acc in range(1,account+1):

            if(acc == 0):
                acc = 1


            subprocess.call("google")
            time.sleep(3)
            keyboard.press_and_release("tab")
            time.sleep(0.5)
            keyboard.write(self.url)
            keyboard.press_and_release("enter")
            time.sleep(3)



            #########################



            keyboard.write(self.accounts[str(acc)][self.username])
            keyboard.press_and_release("tab")
            keyboard.write(self.accounts[str(acc)][self.password])
            keyboard.press_and_release("enter")
            time.sleep(10)


            self.Get_Mail.set_mail(mail_addres=self.accounts[str(acc)][self.mail], password=self.accounts[str(acc)][self.password_mail])

            time.sleep(1)
            keyboard.write(self.Get_Mail.Mail.code)



            keyboard.press("shift")
            time.sleep(0.1)
            keyboard.press_and_release("tab")
            time.sleep(0.1)
            keyboard.release("shift")
            time.sleep(0.1)

            keyboard.press_and_release("enter")
            time.sleep(3)

            keyboard.press_and_release("tab")
            time.sleep(0.5)





            keyboard.press("shift")
            keyboard.press_and_release("m")
            keyboard.release("shift")
            keyboard.press_and_release("o")
            keyboard.press_and_release("n")
            keyboard.press_and_release("t")
            keyboard.press_and_release("a")
            keyboard.press_and_release("n")
            keyboard.press_and_release("a")
            keyboard.press("shift")
            keyboard.press_and_release("b")
            keyboard.release("shift")
            keyboard.press_and_release("l")
            keyboard.press_and_release("a")
            keyboard.press_and_release("c")
            keyboard.press_and_release("k")
            keyboard.press_and_release("8")
            keyboard.press_and_release("8")



            time.sleep(2)
            keyboard.press_and_release("down arrow")
            keyboard.press_and_release("down arrow")
            keyboard.press_and_release("down arrow")
            keyboard.press_and_release("enter")

            time.sleep(5)







if __name__ == "__main__":
    Twitch = Twitch_log()
    Twitch.log(3)