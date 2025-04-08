import requests
from bs4 import BeautifulSoup

chronic_category_parser_urls = [#'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html', 
                        #'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html', 
                        #'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html', 
                        #'https://www.interfax.ru/chronicle/zaderzhanie-gubernatora-habarovskogo-kraya-sergeya-furgala.html', 
                        #'https://www.interfax.ru/chronicle/napadeniya-v-shkolah.html', 'https://www.interfax.ru/chronicle/putin-pryamaya-liniya-2023.html', 
                        #'https://www.interfax.ru/chronicle/ataka-bespilotnikov-na-moskvu.html', 'https://www.interfax.ru/chronicle/delo-protiv-sovetnika-glavy-roskosmosa-ivana-safronova.html', 
                        'https://www.interfax.ru/chronicle/delo-penzenskogo-gubernatora-belozerczeva.html', 'https://www.interfax.ru/chronicle/diplomaticheskoe-protivostoyanie.html']

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }


chronicles = []


def get_chronicle(url):
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        main_div = soup.find('div', class_='chronicles')
        if main_div:
            name = main_div.find('h1').text
            photo = main_div.find('img')['src']
            description = main_div.find('div', class_ = 'chronicles__text').text
            slug = list(list(url.split('/'))[4].split('.'))[0]
            chronicles.append({'name': name, 'photo': photo, 'description': description, 'slug': slug})
            print(slug)
    return chronicles


if __name__ == '__main__':
    file = open('chronicle.json', 'w', encoding='utf-8')
    for url in chronic_parser_urls:
        chronicles = get_chronicle(url)
        file.write(str(chronicles))
    file.close()