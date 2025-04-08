import datetime
import time

import requests
from bs4 import BeautifulSoup

url = 'https://www.interfax.ru'

daily_parser_urls = ['https://www.interfax.ru/russia/', 'https://www.interfax.ru/world/', 'https://www.interfax.ru/business/',
               'https://www.interfax.ru/culture/', 'https://www.interfax.ru/moscow/', 'https://www.interfax.ru/digital/']

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }

main_news_class = 'timeline__group'
text_news_class = 'timeline__text'
photo_news_class = 'timeline__photo'
smalltext_news_class = 'timeline__smalltext'


def daily_main_news(url, tag_class):
    resp = requests.get(url, headers=headers)
    news = []
    n = 0
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        main_div = soup.find('div', class_='timeline')
        if main_div:
            div_list = main_div.find_all('div', class_=tag_class)
            for div in div_list:
                if div.find('time')['datetime'][:10] == str(datetime.date.today()):
                    title = div.find('h3').text
                    a_list = div.find_all('a')
                    created_at = div.find('time')['datetime']
                    for a in a_list:
                        if not a.find('h3'):
                            continue
                        else:
                            href = a['href']
                            category = list(href.split('/'))[1]
                            news_id = list(href.split('/'))[2]
                        if category == '':
                            continue
                        else:
                            new_url = url + '/' + news_id
                            new_resp = requests.get(new_url, headers=headers)
                            text = []
                            if new_resp.status_code == 200:
                                soup = BeautifulSoup(new_resp.content, 'html.parser')
                                div = soup.find('article')
                                if div:
                                    p_list = div.find_all('p')
                                    for p in p_list:
                                        p = p.text + '& '
                                        text.append(p)
                            description = ''
                            for p in text:
                                description += p
                    news.append({'title': title, 'description': description, 'created_at': created_at, 'name': category, 'photo': 0})
                    n += 1
                    time.sleep(3)
                else:
                    continue
        else:
            print('Разметка была изменена')
    else:
        print('Страница не отвечает')
    print("Новости 1", n)
    return news


def daily_photo_news(url, tag_class):
    resp = requests.get(url, headers=headers)
    news = []
    n = 0
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        main_div = soup.find('div', class_='timeline')
        if main_div:
            div_list = main_div.find_all('div', class_=tag_class)
            for div in div_list:
                if div.find('time')['datetime'][:10] == str(datetime.date.today()):
                    photo = div.find('img')['src']
                    title = div.find('h3').text
                    href = div.find('a')['href']
                    category = list(href.split('/'))[1]
                    news_id = list(href.split('/'))[2]
                    if category == '':
                        continue
                    else:
                        created_at = div.find('time')['datetime']
                        new_url = url + '/' + news_id
                        new_resp = requests.get(new_url, headers=headers)
                        text = []
                        if new_resp.status_code == 200:
                            soup = BeautifulSoup(new_resp.content, 'html.parser')
                            div = soup.find('article')
                            if div:
                                p_list = div.find_all('p')
                                for p in p_list:
                                    p = p.text + '& '
                                    text.append(p)
                        description = ''
                        for p in text:
                            description += p
                        news.append({'title': title, 'description': description, 'created_at': created_at, 'name': category, 'photo': photo})
                        n += 1
                        time.sleep(3)
                else:
                    continue
        else:
            print('Разметка была изменена')
    else:
        print('Страница не отвечает')
    print("Новости 2", n)
    return news


if __name__ == '__main__':
    file = open('word.json', 'w', encoding='utf-8')
    for url in daily_parser_urls:
        news = daily_main_news(url, main_news_class)
        text_news = daily_main_news(url, text_news_class)
        smalltext_news = daily_main_news(url, smalltext_news_class)
        news_photo = daily_photo_news(url, photo_news_class)
        file.write(str(news))
        file.write(str(text_news))
        file.write(str(news_photo))
        file.write(str(smalltext_news))
    file.close()