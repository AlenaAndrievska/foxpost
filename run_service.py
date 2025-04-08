import django
#from parser_app.parsers import main_news, currency_rate, photo_news, main_news_class, text_news_class, photo_news_class, \
#    get_categories, parser_urls
from parser_app.parsers.currency_parser import currency_rate
from parser_app.parsers.category_parser import get_categories, url
from parser_app.parsers.main_parser import main_news, photo_news, main_news_class, text_news_class, photo_news_class, \
    parser_urls_world_10
from parser_app.parsers.chronic_category_parser import chronic_category_parser_urls, get_chronicle
from parser_app.parsers.chronicles_parser import chronic_news, chronic_parser_urls, daily_chronic_news, chronic_belozer_parser_urls_01
from parser_app.parsers.photo_parser import photo_archive_news, photo_parser_urls, photo_url, photo_news_daily
from parser_app.parsers.daily_parser import daily_parser_urls, daily_main_news, daily_photo_news
from parser_app.parsers.sport_parser import sport_urls_02, main_sport_news, photo_sport_news, daily_main_sport_news, daily_photo_sport_news, sport_url
import os
import sys
from django.db import DatabaseError
import datetime
import transliterate


proj = os.path.dirname((os.path.abspath(__file__)))
sys.path.append((proj))
os.environ['DJANGO_SETTINGS_MODULE'] = 'fox_project.settings'
django.setup()


from parser_app.models import Articles, Category, Currency, ChronicleCategory, ChronicleArticles


news = []
categories = get_categories(url)
chronicles = []
chronicle_news = []

def chronicles_add(chronicles):
    for url in chronic_category_parser_urls:
        i = get_chronicle(url)
        chronicles += i
    for chr in chronicles:
        chronicle_instance = ChronicleCategory(**chr)
        try:
            chronicle_instance.save()
        except DatabaseError:
            print('Ошибка')
            pass

def category_add(categories):
    for cat in categories:
        category_instance = Category(**cat)
        try:
            category_instance.save()
        except DatabaseError:
            pass


def currency_add(url):
    currency = currency_rate(url)
    currency_model = Currency(**currency[0])
    currency_model.save()


def chronicle_articles_add(chronicle_news):
    for url in chronic_parser_urls:
    #for url in chronic_belozer_parser_urls_01:
        chr = daily_chronic_news(url)
        #chr = chronic_news(url)
        chronicle_news += chr
    for elem in chronicle_news:
        if ChronicleCategory.objects.filter(slug=elem['chronicle_name']).exists():
            chr_instance = ChronicleCategory.objects.get(slug=elem['chronicle_name'])
            slug = transliterate.slugify(elem['title'], 'ru')
            art = ChronicleArticles(**elem, chronicle=chr_instance, slug=slug)
            try:
                art.save()
            except DatabaseError:
                pass
        else:
            print('Ошибка')
            continue

def articles_add(daily_parser_urls, news):
    for url in sport_url:
        i_sport = daily_main_sport_news(url, main_news_class)
        news += i_sport
        j_sport = daily_photo_sport_news(url, photo_news_class)
        news += j_sport
        y_sport = daily_main_sport_news(url, text_news_class)
        news += y_sport
    #for url in photo_parser_urls:
    #photo = photo_news_daily(photo_url)
    photo = photo_archive_news(photo_url)
    news += photo
    for url in daily_parser_urls:
        i = daily_main_news(url, main_news_class)
        news += i
        j = daily_main_news(url, text_news_class)
        news += j
        y = daily_photo_news(url, photo_news_class)
        news += y
    for elem in news:
        if Category.objects.filter(slug=elem['name']).exists():
            cat_instance = Category.objects.get(slug=elem['name'])
            slug = transliterate.slugify(elem['title'], 'ru')
            art = Articles(**elem, category=cat_instance, slug=slug)
            print(art)
            try:
                art.save()
            except DatabaseError:
                pass
                print('Ошибка DB')
        else:
            print('Ошибка')
            continue


if __name__ == '__main__':
    #category_add(categories)
    #currency_add(url)
    #chronicles_add(chronicles)
    #articles_add(sport_url, news)
    articles_add(daily_parser_urls, news)
    chronicle_articles_add(chronicle_news)
    print('Done')

