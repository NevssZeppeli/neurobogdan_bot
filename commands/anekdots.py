import requests, random
from bs4 import BeautifulSoup

def anekdot():
    anekdot_page = 'https://www.anekdot.ru/best/anekdot/0107/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'}

    page = requests.get(anekdot_page, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    convert = soup.find_all('div', {"class": "text"})

    return convert[random.randint(0, len(convert))].text
