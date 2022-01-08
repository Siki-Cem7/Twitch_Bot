import sys
import time
import webbrowser

import requests
import subprocess
import keyboard
from pynput.keyboard import Key, Controller


class Twitch_log():


    def __init__(self):

        self.username = "username"
        self.password = "password"

        self.url = "https://twitch.tv/login"


        self.accounts = {
            "1": {self.username: "sikicemjackson", self.password: "Internet07dasvierte"},
            "2":{self.username:"dellasderaller", self.password:"IQwww349DF"},
            "3":{self.username:"markoderalleer", self.password:"Hee123dssaL6"}
        }


#11
#14







    def log(self, account):


        for acc in range(account):

            if(acc == 0):
                acc = 1

            subprocess.call("google")
            time.sleep(2)
            for i in range(0, 16):
                keyboard.press_and_release("tab")
                time.sleep(0.1)
            time.sleep(0.4)
            keyboard.write(self.url)
            keyboard.press_and_release("enter")
            time.sleep(3)


            #########################



            for i in range(0,11):
                keyboard.press_and_release("tab")
                time.sleep(0.1)
            keyboard.press_and_release("enter")
            time.sleep(2)
            for i in range(0,14):
                keyboard.press_and_release("tab")
                time.sleep(0.1)
            keyboard.press_and_release("enter")


            time.sleep(4)

            for i in range(0,7):
                keyboard.press_and_release("tab")
                time.sleep(0.1)
            keyboard.press_and_release("enter")

            time.sleep(4)




            keyboard.write(self.accounts[str(acc)][self.username])
            keyboard.press_and_release("tab")
            keyboard.write(self.accounts[str(acc)][self.password])
            keyboard.press_and_release("enter")
            time.sleep(6)



            for i in range(0,3):
                keyboard.press_and_release("tab")
                time.sleep(0.1)
            keyboard.press_and_release("enter")
            time.sleep(3)
            for i in range(0, 13):
                keyboard.press_and_release("tab")
                time.sleep(0.1)
            time.sleep(0.9)
            keyboard.press_and_release("enter")

            time.sleep(3)








if __name__ == "__main__":
    Twitch = Twitch_log()
    Twitch.log(1)