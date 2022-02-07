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
            #"Main": {self.username: "sikicemjackson", self.password: "*************", self.mail:"sommer.silvan3@gmail.com", self.password_mail:"*************"},
            #"1":{self.username:"markoderalleer", self.password:"Hee123dssaL6", self.mail:"bot.trackerreport@gmail.com", self.password_mail:"12345678AaS"},

            "2":{self.username:"dellasderaller", self.password:"IQwww349DF", self.mail:"siki.cemmii@gmail.com", self.password_mail:"Internet07dasvierte"},
            "1":{self.username:"phillippderaller", self.password:"dfrSS349jfhg", self.mail:"wtdddfekomsichg@gmail.com", self.password_mail:"cdksks/()==(sdkf"},
            "3":{self.username:"krebsderaller", self.password:"hHHSF23454jDJJD", self.mail:"krebsderaller@gmail.com", self.password_mail:"dkfsk%&/FFFG"},
            "4":{self.username:"lionderaller", self.password:"HHGT666666788SDD", self.mail:"lionderaller@gmail.com", self.password_mail:"Lkkkpo))894GSJ"},
            "5":{self.username:"Christinderaller", self.password:"christindugeile()()", self.mail:"christinaderaller@gmail.com", self.password_mail:"lakdpQWWER2325"},
            "6":{self.username:"Nurcettzideraller", self.password:"xsAAPjj6432", self.mail:"nurcetzkideraller@gmail.com", self.password_mail:"jjklplBBDF3434"},
            "7":{self.username:"iceteaderaller", self.password:"kppiKKkdk678", self.mail:"iceteaderalller@gmail.com", self.password_mail:"jJJjkkll344334"},
            "8":{self.username:"cpuderaller", self.password:"hhaddERE33332", self.mail:"cpuderalller@gmail.com", self.password_mail:"asdertfASDERZ"},
            "9":{self.username:"karitzideraller", self.password:"HHHkkkdkdkd", self.mail:"karitzideraller@gmail.com", self.password_mail:"Awwwq2888765"},
            "10":{self.username:"beschederaller", self.password:"hGF9343hfhjJDjhjaksd", self.mail:"beschederaller@gmail.com", self.password_mail:"ZZ233234Hfda"},
            "11":{self.username:"coopderaller", self.password:"JJKlpoPPPP", self.mail:"coopderaller@gmail.com", self.password_mail:"DSDdfffff233"},
            "12":{self.username:"patrickderaller", self.password:"hhhTTTR567373", self.mail:"patrickderaller@gmail.com", self.password_mail:"hjkjdlPPPOP9889"},
            "13":{self.username:"harveyderaller", self.password:"Aaasd325AAsfffffJKDKFH", self.mail:"harveyderaller@gmail.com", self.password_mail:"hg67654GGGfdtr"},
            "14":{self.username:"michaelderaller", self.password:"halKKPOU8646238", self.mail:"michaealderaller@gmail.com", self.password_mail:"wREQZhfgs5456"}
        }






    def log(self, account):


        for acc in range(1,account+1):

            if(acc == 0):
                acc = 1


            subprocess.call("google")
            time.sleep(2.5)
            keyboard.press_and_release("tab")
            time.sleep(0.5)
            keyboard.write(self.url)
            keyboard.press_and_release("enter")
            time.sleep(2)



            #########################



            keyboard.write(self.accounts[str(acc)][self.username])
            keyboard.press_and_release("tab")
            keyboard.write(self.accounts[str(acc)][self.password])
            keyboard.press_and_release("enter")
            time.sleep(6)


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
            time.sleep(2.5)

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



            time.sleep(2.5)
            keyboard.press_and_release("down arrow")
            keyboard.press_and_release("down arrow")
            keyboard.press_and_release("down arrow")
            keyboard.press_and_release("enter")
            time.sleep(2)


            if(acc == 8):
                input("VPN connection >> ")



if __name__ == "__main__":
    Twitch = Twitch_log()
    Twitch.log(1)