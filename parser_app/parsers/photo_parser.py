import locale
import datetime
import time
from django.utils import timezone
import pytz

import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

timezone.activate(pytz.timezone('Europe/Moscow'))

RU_MONTH_VALUES = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 10,
    'декабря': 12,
}


photo_parser_urls = []
photo_url = 'https://www.interfax.ru/photo/'

for page in range(101, 70, -1):
    url = 'https://www.interfax.ru/photo/archive/page_' + str(page)
    photo_parser_urls.append(url)


def photo_archive_news(url):
    resp = requests.get(url, headers=headers)
    photos = []
    n = 0
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        main_div = soup.find('div', class_='photoindex')
        if main_div:
            a_list = main_div.find_all('a')
            for a in a_list[:5]:
                href = a['href']
                new_url = 'https://www.interfax.ru' + href
                print(new_url)
                new_resp = requests.get(new_url, headers=headers)
                if new_resp.status_code == 200:
                    soup = BeautifulSoup(new_resp.content, 'html.parser')
                    div = soup.find('div', class_='photobox')
                    if div and div.find('div', class_='photo__date'):
                        title = div.find('h1').text
                        created_at = list(div.find('div', class_='photo__date').text[13:-5].split(' '))
                        month = created_at[1]
                        dig_month = RU_MONTH_VALUES.get(month)
                        created_at = datetime.datetime.strptime(str(created_at[2] + '-' + created_at[0] + '-' + str(dig_month)), '%Y-%d-%m')
                        created_at = created_at.replace(tzinfo=pytz.UTC)
                        figure = div.find('figure')
                        if figure:
                            photo = figure.find('img')['src']
                            text = figure.find('div', class_='desc').text
                            author = figure.find('div', class_='author').text
                            description = text + ' & ' + 'Автор: ' + author
                            photos.append({'title': title, 'photo': photo, 'description': description, 'name': 'photo',
                                     'created_at': created_at})
                    else:
                        continue
                else:
                    print('Страница не отвечает')
                n += 1
        else:
            print('Разметка была изменена')
    else:
        print('Страница не отвечает')
    print("Новости", n)
    return photos
    

def photo_news_daily(url):
    resp = requests.get(url, headers=headers)
    photos = []
    n = 0
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        main_div = soup.find('div', class_='photoindex')
        if main_div:
            a_list = main_div.find_all('a')
            for a in a_list[:2]:
                href = a['href']
                new_url = 'https://www.interfax.ru' + href
                new_resp = requests.get(new_url, headers=headers)
                if new_resp.status_code == 200:
                    soup = BeautifulSoup(new_resp.content, 'html.parser')
                    div = soup.find('div', class_='photobox')
                    if div and div.find('div', class_='photo__date'):
                        created_at = list(div.find('div', class_='photo__date').text[13:-5].split(' '))
                        month = created_at[1]
                        dig_month = RU_MONTH_VALUES.get(month)
                        created_at = datetime.datetime.strptime(str(created_at[2] + '-' + created_at[0] + '-' + str(dig_month)), '%Y-%d-%m')
                        print(created_at.date(), str(datetime.date.today()))
                        if created_at.date() == str(datetime.date.today()):
                            title = div.find('h1').text
                            figure_list = div.find_all('figure')
                            for figure in figure_list:
                                photo = figure.find('img')['src']
                                text = figure.find('div', class_='desc').text
                                author = figure.find('div', class_='author').text
                                description = text + ' & ' + 'Автор: ' + author
                                photos.append({'title': title, 'photo': photo, 'description': description, 'name': 'photo',
                                        'created_at': created_at})
                                print(text)
                            print(title)
                    else:
                        continue
                else:
                    print('Страница не отвечает')
                n += 1
                time.sleep(3)
        else:
            print('Разметка была изменена')
    else:
        print('Страница не отвечает')
    print("Новости", n)
    return photos

if __name__ == '__main__':
    file = open('photo.json', 'w', encoding='utf-8')
    #for url in photo_parser_urls:
    news = photo_archive_news(photo_url)
    file.write(str(news))
    file.close()