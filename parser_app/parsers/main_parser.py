import time

import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }

main_news_class = 'timeline__group'
text_news_class = 'timeline__text'
photo_news_class = 'timeline__photo'

parser_urls_russia = ['https://www.interfax.ru/russia/', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-12-14T06:55',
                      'https://www.interfax.ru/russia/?a=mainblock&dt=2023-12-13T15:36', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-12-12T15:46',
                      'https://www.interfax.ru/russia/?a=mainblock&dt=2023-12-12T10:57', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-12-11T13:37',
                      'https://www.interfax.ru/russia/?a=mainblock&dt=2023-12-10T09:31', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-12-08T14:19',]

parser_urls_russia_01 = ['https://www.interfax.ru/russia/?a=mainblock&dt=2023-12-08T00:05', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-12-07T15:17',
                         'https://www.interfax.ru/russia/?a=mainblock&dt=2023-12-07T11:09', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-12-06T15:27',
                         'https://www.interfax.ru/russia/?a=mainblock&dt=2023-12-05T21:55', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-12-05T14:27',
                         'https://www.interfax.ru/russia/?a=mainblock&dt=2023-12-03T14:47', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-12-01T20:21',]

parser_urls_russia_02 = ['https://www.interfax.ru/russia/?a=mainblock&dt=2023-12-01T09:28', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-30T16:13',
                         'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-29T20:26', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-29T12:41',
                         'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-28T15:32', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-28T09:19',
                         'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-27T09:19', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-26T11:53',]

parser_urls_russia_03 = ['https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-24T19:38', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-23T18:26',
                         'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-23T09:45', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-22T13:50',
                         'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-21T19:11', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-21T09:05',
                         'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-20T12:31', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-19T07:55',]

parser_urls_russia_04 = ['https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-17T16:48', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-16T18:59',
                         'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-16T12:27', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-15T14:53',
                         'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-13T17:56', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-12T16:45',
                         'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-10T17:08', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-10T03:15',]

parser_urls_russia_05 = ['https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-09T14:34', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-08T16:54',
                         'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-08T09:53', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-07T08:20',
                         'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-04T16:50', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-03T14:39',
                         'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-02T17:55', 'https://www.interfax.ru/russia/?a=mainblock&dt=2023-11-02T09:17',]

parser_urls_world_01 = ['https://www.interfax.ru/world/', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-12-18T02:49', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-12-16T03:03', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-12-15T10:12', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-12-14T15:47', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-12-13T20:53',]

parser_urls_world_02 = ['https://www.interfax.ru/world/?a=mainblock&dt=2023-12-13T03:37', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-12-12T12:48', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-12-11T15:21', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-12-10T12:54', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-12-08T17:53', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-12-08T05:59',]
                        
parser_urls_world_03 = ['https://www.interfax.ru/world/?a=mainblock&dt=2023-12-07T14:09', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-12-06T22:28',
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-12-06T11:57', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-12-05T16:06', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-12-04T22:15', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-12-04T07:14', ]
                        
parser_urls_world_04 = ['https://www.interfax.ru/world/?a=mainblock&dt=2023-12-02T05:04', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-12-01T13:16', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-30T17:38', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-30T10:38', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-29T17:10', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-29T01:46',]
                        
parser_urls_world_05 = ['https://www.interfax.ru/world/?a=mainblock&dt=2023-11-28T13:10', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-27T16:25', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-26T14:40', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-24T20:43', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-24T11:28', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-23T12:59',]
                        
parser_urls_world_06 = ['https://www.interfax.ru/world/?a=mainblock&dt=2023-11-22T17:01', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-22T08:19', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-21T15:32', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-20T19:41', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-20T03:41', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-18T13:34',]

parser_urls_world_07 = ['https://www.interfax.ru/world/?a=mainblock&dt=2023-11-17T16:29', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-17T00:57', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-16T12:18', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-15T19:27', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-15T06:26', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-14T11:01',]
                        
parser_urls_world_08 = ['https://www.interfax.ru/world/?a=mainblock&dt=2023-11-13T15:30', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-12T14:26', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-10T21:41', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-10T07:54', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-09T15:36', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-08T16:53',]
                        
parser_urls_world_09 = ['https://www.interfax.ru/world/?a=mainblock&dt=2023-11-07T18:33', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-07T05:32', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-06T04:05', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-04T08:39', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-03T12:15', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-02T17:13',]
                        
parser_urls_world_10 = ['https://www.interfax.ru/world/?a=mainblock&dt=2023-11-01T22:27', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-11-01T09:52', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-10-31T14:32', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-10-30T17:36', 
                        'https://www.interfax.ru/world/?a=mainblock&dt=2023-10-29T13:38', 'https://www.interfax.ru/world/?a=mainblock&dt=2023-10-28T06:27', ]
                        

parser_urls_business_01 = ['https://www.interfax.ru/business/', ]

parser_urls_culture_01 = ['https://www.interfax.ru/culture/', 'https://www.interfax.ru/culture/?a=mainblock&dt=2023-11-20T12:01', 
                        'https://www.interfax.ru/culture/?a=mainblock&dt=2023-10-17T11:43', 'https://www.interfax.ru/culture/?a=mainblock&dt=2023-09-09T16:15',
                        'https://www.interfax.ru/culture/?a=mainblock&dt=2023-07-26T16:08',]

parser_urls_moscow_01 = ['https://www.interfax.ru/moscow/', 'https://www.interfax.ru/moscow/?a=mainblock&dt=2023-12-08T18:48', 
                        'https://www.interfax.ru/moscow/?a=mainblock&dt=2023-11-30T17:18', 'https://www.interfax.ru/moscow/?a=mainblock&dt=2023-11-21T18:16', 
                        'https://www.interfax.ru/moscow/?a=mainblock&dt=2023-11-09T10:16', 'https://www.interfax.ru/moscow/?a=mainblock&dt=2023-10-28T11:47',]
                        
parser_urls_moscow_02 = ['https://www.interfax.ru/moscow/?a=mainblock&dt=2023-10-19T17:56', 'https://www.interfax.ru/moscow/?a=mainblock&dt=2023-10-09T09:21',
                        'https://www.interfax.ru/moscow/?a=mainblock&dt=2023-10-02T11:08', 'https://www.interfax.ru/moscow/?a=mainblock&dt=2023-09-19T13:13', 
                        'https://www.interfax.ru/moscow/?a=mainblock&dt=2023-09-09T13:53', 'https://www.interfax.ru/moscow/?a=mainblock&dt=2023-08-31T11:17',]

parser_urls_moscow_03 = ['https://www.interfax.ru/moscow/?a=mainblock&dt=2023-08-25T14:52', 'https://www.interfax.ru/moscow/?a=mainblock&dt=2023-08-21T16:28', 
                        'https://www.interfax.ru/moscow/?a=mainblock&dt=2023-08-17T09:53', ]
                        

parser_urls_digital_01 = ['https://www.interfax.ru/digital/', 'https://www.interfax.ru/digital/?a=mainblock&dt=2023-11-28T16:09', 
                        'https://www.interfax.ru/digital/?a=mainblock&dt=2023-11-13T16:03', 'https://www.interfax.ru/digital/?a=mainblock&dt=2023-10-25T17:04',
                        'https://www.interfax.ru/digital/?a=mainblock&dt=2023-10-06T14:33', 'https://www.interfax.ru/digital/?a=mainblock&dt=2023-09-20T15:56', 
                        'https://www.interfax.ru/digital/?a=mainblock&dt=2023-08-29T10:06', 'https://www.interfax.ru/digital/?a=mainblock&dt=2023-08-15T13:41', ]



def main_news(url, tag_class):
    resp = requests.get(url, headers=headers)
    news = []
    n = 0
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        main_div = soup.find('div', class_='timeline')
        if main_div:
            div_list = main_div.find_all('div', class_=tag_class)
            for div in div_list:
                art_list = div.find_all('div')
                for div in art_list:
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
                            new_url = 'https://www.interfax.ru/' + category + '/' + news_id
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
                        news.append({'title': title, 'description': description, 'created_at': created_at, 'name': category,
                                 'photo': 0})
                    n += 1
                    time.sleep(4)
        else:
            print('Разметка была изменена')
    else:
        print('Страница не отвечает')
    print("Новости 1", n)
    return news


def photo_news(url, tag_class):
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
                category = list(href.split('/'))[1]
                news_id = list(href.split('/'))[2]
                if category == '':
                    continue
                else:
                    time = div.find('time')['datetime']
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
                    news.append({'title': title, 'description': description, 'created_at': time, 'name': category,
                                 'photo': photo})
                    print(category)
                    n += 1
        else:
            print('Разметка была изменена')
    else:
        print('Страница не отвечает')
    print("Новости 2", n)
    return news


if __name__ == '__main__':
    file = open('word.json', 'w', encoding='utf-8')
    for url in parser_urls_russia:
        news = main_news(url, main_news_class)
        text_news = main_news(url, text_news_class)
        news_photo = photo_news(url, photo_news_class)
        file.write(str(news))
        file.write(str(text_news))
        file.write(str(news_photo))
    file.close()