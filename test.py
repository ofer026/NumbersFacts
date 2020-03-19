
from bs4 import BeautifulSoup as bsoup
import requests

#URL = "http://numbersapi.com/04/11/date"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.57756"}
class get_data:

    def __init__(self):
        self.URL = URL
        self.page = requests.get(self.URL, headers=headers)
        self.soup = bsoup(self.page.content, 'html.parser')
    def get_info(self):
        return self.soup

    #print(soup)
