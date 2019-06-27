import requests
from bs4 import BeautifulSoup
from datetime import datetime
url = "http://www.cbr.ru/scripts/XML_daily.asp"
today = datetime.now().strftime("%d/%m/%Y")
payload = {"data_req": today}
response = requests.get(url, params = payload)
soup = BeautifulSoup(response.content, "lxml")

def get_course(id):
    return str(soup.find("valute", {"id": id}).value.text)