from django import template

register = template.Library()


@register.filter(name='split')
def split(value, splitter):
    return value.split(splitter)

@register.filter(name='prev')
def prev(articles, article):
    n = 0
    for art in articles:
        n += 1
        if art == article:
            prev_num = n-2
            prev = articles[prev_num]
            return prev