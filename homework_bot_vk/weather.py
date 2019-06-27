import requests
import bs4

def get_content(city):
    url = "https://yandex.ru/pogoda/" + city
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, "lxml")
    return soup

def get_temp(soup):
    result = soup.find("span", {"class": "temp__value"})
    return result.text

def get_condition(soup):
    result = soup.find("div", {"class": "link__condition"})
    return result.text

def get_wind(soup):
    result = soup.find("span", {"class": "wind-speed"})
    return result.text

def get_humidity(soup):
    result = soup.find("dl", {"class": "term term_orient_v fact__humidity"})
    return result.text
def get_pressure(soup):
    result = soup.find("dl", {"class": "term term_orient_v fact__pressure"})
    return result.text
def main(city):
    soup = get_content(city)

    weather = (get_temp(soup)) + " " + (get_condition(soup)) + " " +(get_wind(soup) + " м/с")+ " "  + (get_humidity(soup))+ " " + (get_pressure(soup))
    return weather

