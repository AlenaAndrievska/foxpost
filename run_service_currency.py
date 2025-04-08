import django
from parser_app.parsers.currency_parser import currency_rate
from parser_app.parsers.category_parser import url
import os
import sys


proj = os.path.dirname((os.path.abspath(__file__)))
sys.path.append((proj))
os.environ['DJANGO_SETTINGS_MODULE'] = 'fox_project.settings'
django.setup()


from parser_app.models import Currency


def currency_add(url):
    currency = currency_rate(url)
    currency_model = Currency(**currency[0])
    currency_model.save()


if __name__ == '__main__':
    currency_add(url)
    print('Done')