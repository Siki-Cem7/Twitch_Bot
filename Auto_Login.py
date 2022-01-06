import requests
import json
from bs4 import BeautifulSoup
import webbrowser



class Twitch_log():


    def __init__(self):

        self.url = "https://passport.twitch.tv/login"
        self.payload = {"username": "sikicemjackson", "password": "Internet07dasvierte"}
        self.url_get = "https://www.twitch.tv/?no-reload=true"




    def log(self):

        self.s = requests.Session()
        self.resp = self.s.post(url=self.url, json=self.payload)
        print(self.resp.text)


        #self.s.headers.update({"authorization":json.loads(self.resp.content)["token"]})
        #print(self.resp.content)








if __name__ == "__main__":
    Twitch = Twitch_log()
    Twitch.log()
