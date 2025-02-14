from bs4 import BeautifulSoup
import requests

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    soup_list = soup.find_all('tr')

    for element in soup_list:
        if "USD" in element.text:
            cells = element.find_all('td')
            if len(cells) > 4:
                usd_rate = cells[4].text.strip()
                print(f"Курс долара: {usd_rate} грн")

