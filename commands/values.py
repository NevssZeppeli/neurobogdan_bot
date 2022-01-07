import requests
from bs4 import BeautifulSoup


def dollar():
    dollar_to_rub = "https://www.google.com/search?client=firefox-b-d&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'}

    page = requests.get(dollar_to_rub, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    convert = soup.find_all("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

    return "Курс доллара равен " + str(convert[0].text) + "р за одну штуку."


def euro():
    euro_to_rub = "https://www.google.com/search?client=firefox-b-d&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'}

    page = requests.get(euro_to_rub, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    convert = soup.find_all("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

    return "Курс евро равен " + str(convert[0].text) + "р за одну штуку."
