import requests
from bs4 import BeautifulSoup
import datetime
import time

sport_url = ['https://www.sport-interfax.ru', ]

sport_urls = ['https://www.sport-interfax.ru', 'https://www.sport-interfax.ru/?a=mainblock&dt=2023-12-05T19:20', 
            'https://www.sport-interfax.ru/?a=mainblock&dt=2023-11-26T17:10', 'https://www.sport-interfax.ru/?a=mainblock&dt=2023-11-20T15:30', 
            'https://www.sport-interfax.ru/?a=mainblock&dt=2023-11-14T17:00', 'https://www.sport-interfax.ru/?a=mainblock&dt=2023-11-08T20:21', ]
            
            
sport_urls_01 = ['https://www.sport-interfax.ru/?a=mainblock&dt=2023-11-01T10:41', 'https://www.sport-interfax.ru/?a=mainblock&dt=2023-10-25T22:19', 
                'https://www.sport-interfax.ru/?a=mainblock&dt=2023-10-19T23:54', 'https://www.sport-interfax.ru/?a=mainblock&dt=2023-10-13T17:12', ]
                
sport_urls_02 = ['https://www.sport-interfax.ru/?a=mainblock&dt=2023-10-07T21:03', 'https://www.sport-interfax.ru/?a=mainblock&dt=2023-10-01T00:29', 
                'https://www.sport-interfax.ru/?a=mainblock&dt=2023-09-24T21:09',]

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }

main_news_class = 'timeline__group'
text_news_class = 'timeline__text'
photo_news_class = 'timeline__photo'


def main_sport_news(url, tag_class):
    resp = requests.get(url, headers=headers)
    news = []
    n = 0
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        main_div = soup.find('div', class_='timeline')
        if main_div:
            div_list = main_div.find_all('div', class_=tag_class)
            for div in div_list:
                title = div.find('h3').text
                href = div.find('a')['href']
                created_at = div.find('time')['datetime']
                new_url = 'https://www.sport-interfax.ru' + '/' + href
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
                news.append({'title': title, 'description': description, 'created_at': created_at, 'name': 'sport',
                             'photo': 0})
                n += 1
                time.sleep(4)
        else:
            print('Разметка была изменена')
    else:
        print('Страница не отвечает')
    print("Новости 1", n)
    return news


def daily_main_sport_news(url, tag_class):
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
                    href = div.find('a')['href']
                    created_at = div.find('time')['datetime']
                    new_url = 'https://www.sport-interfax.ru' + '/' + href
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
                    news.append({'title': title, 'description': description, 'created_at': created_at, 'name': 'sport',
                             'photo': 0})
                    n += 1
                    time.sleep(4)
        else:
            print('Разметка была изменена')
    else:
        print('Страница не отвечает')
    print("Новости 1", n)
    return news
    

def photo_sport_news(url, tag_class):
    resp = requests.get(url, headers=headers)
    news = []
    n = 0
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        main_div = soup.find('div', class_='timeline')
        if main_div:
            div_list = main_div.find_all('div', class_=tag_class)
            for div in div_list:
                photo = div.find('img')['src']
                title = div.find('h3').text
                href = div.find('a')['href']
                created_at = div.find('time')['datetime']
                new_url = 'https://www.sport-interfax.ru' + '/' + href
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
                news.append({'title': title, 'description': description, 'created_at': created_at, 'name': 'sport',
                             'photo': photo})
                n += 1
                time.sleep(4)
        else:
            print('Разметка была изменена')
    else:
        print('Страница не отвечает')
    print("Новости 2", n)
    return news
    
def daily_photo_sport_news(url, tag_class):
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
                    created_at = div.find('time')['datetime']
                    new_url = 'https://www.sport-interfax.ru' + '/' + href
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
                    news.append({'title': title, 'description': description, 'created_at': created_at, 'name': 'sport',
                             'photo': photo})
                    n += 1
                    time.sleep(4)
        else:
            print('Разметка была изменена')
    else:
        print('Страница не отвечает')
    print("Новости 2", n)
    return news


if __name__ == '__main__':
    file = open('word.json', 'w', encoding='utf-8')
    for url in sport_urls:
        news = main_sport_news(url, main_news_class)
        text_news = main_sport_news(url, text_news_class)
        news_photo = photo_sport_news(url, photo_news_class)
        file.write(str(news))
        file.write(str(text_news))
        file.write(str(news_photo))
    file.close()