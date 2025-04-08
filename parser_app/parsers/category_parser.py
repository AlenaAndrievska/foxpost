import requests
from bs4 import BeautifulSoup

url = 'https://www.interfax.ru'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }


def get_categories(url):
    resp = requests.get(url, headers=headers)
    categories = []
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        main_div = soup.find('div', class_='toplinks').find('nav')
        if main_div:
            div_list = main_div.find_all('a')
            for div in div_list:
                if div.find('h2'):
                    link = div['href']
                    if link == 'https://www.sport-interfax.ru/':
                        name = div.find('h2').text
                        slug = 'sport'
                    elif link.startswith('/') and len(link) > 1:
                        name = div.find('h2').text
                        slug = link[1:len(link) - 1]
                    else:
                        continue
                else:
                    continue
                categories.append({'name': name, 'slug': slug})
        else:
            print('Разметка была изменена')
    else:
        print('Страница не отвечает')
    return categories


if __name__ == '__main__':
    file = open('categories.json', 'w', encoding='utf-8')
    categories = get_categories(url)
    file.write(str(categories))
    file.close()