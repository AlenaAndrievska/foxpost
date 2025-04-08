import datetime

import requests
from bs4 import BeautifulSoup

url = 'https://www.interfax.ru'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }


def currency_rate(url):
    resp = requests.get(url, headers=headers)
    currency = []
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        div = soup.find('table', class_='rates')
        if div:
            cur_list = div.find_all('td', class_='rate')
            dif_list = div.find_all('td', class_='rate_p')
            date = datetime.datetime.strptime((div.find('td', class_='rate_date').text + '.2023'), '%d.%m.%Y')
            dollar = cur_list[0].text
            euro = cur_list[1].text
            dollar_diff = dif_list[0].text
            euro_diff = dif_list[1].text
            currency.append({'dollar': dollar, 'euro': euro, 'dollar_diff': dollar_diff,
                             'euro_diff': euro_diff, 'date': date})
        else:
            print('Данные не найдены')
    else:
        print('Страница не отвечает')
    return currency

if __name__ == '__main__':
    currency = currency_rate(url)
    file = open('word.json', 'w', encoding='utf-8')
    file.write(str(currency))
    file.close()