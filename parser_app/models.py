from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    """Модель категорий новостей"""
    name = models.CharField(max_length=100, verbose_name='name')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.name}'



class ChronicleCategory(models.Model):
    """Модель категорий новостей раздела Хроники"""
    name = models.CharField(max_length=100, verbose_name='name')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(max_length=10000, verbose_name='description')
    photo = models.CharField(max_length=1000, verbose_name='photo')

    class Meta:
        db_table = 'chronicle'
        verbose_name = 'chronicle'
        verbose_name_plural = 'chronicles'

    def __str__(self):
        return f'{self.name}'



class Articles(models.Model):
    """Модель новостей"""
    title = models.CharField(max_length=100, db_index=True, verbose_name='title')
    description = models.TextField(max_length=10000, verbose_name='description')
    created_at = models.DateTimeField(verbose_name='created_at')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=100, verbose_name='category')
    name = models.CharField(max_length=100, verbose_name='name')
    photo = models.CharField(max_length=1000, verbose_name='photo')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        db_table = 'article'
        verbose_name = 'article'
        verbose_name_plural = 'articles'

    def __str__(self):
        return f'{self.title}'


class ChronicleArticles(models.Model):
    """Модель новостей Хроники"""
    title = models.CharField(max_length=100, db_index=True, verbose_name='title')
    description = models.TextField(max_length=10000, verbose_name='description')
    created_at = models.DateTimeField(verbose_name='created_at')
    chronicle = models.ForeignKey(ChronicleCategory, on_delete=models.SET_NULL, null=True, max_length=100, verbose_name='chronicle')
    chronicle_name = models.CharField(max_length=100, verbose_name='chronicle_name', default=None)
    photo = models.CharField(max_length=1000, verbose_name='photo')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        db_table = 'chronicle_article'
        verbose_name = 'chronicle_article'
        verbose_name_plural = 'chronicle_articles'

    def __str__(self):
        return f'{self.title}'


class Currency(models.Model):
    """Модель курсов валют"""
    date = models.DateField(verbose_name='date')
    dollar = models.CharField(max_length=100, verbose_name='dollar')
    euro = models.CharField(max_length=100, verbose_name='euro')
    dollar_diff = models.CharField(max_length=100, verbose_name='dollar_diff')
    euro_diff = models.CharField(max_length=100, verbose_name='euro_diff')
    day = models.DateField(auto_now=True, verbose_name='day')

    class Meta:
        db_table = 'currency'
        verbose_name = 'currency'
        verbose_name_plural = 'currency'


class Comment(models.Model):
    """Модель комментрария к статье"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='user')
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='comments', verbose_name='article')
    text = models.TextField(verbose_name='text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')

    class Meta:
        db_table = 'comment'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return f"Comment for {self.article} by {self.user}"


class ChronicleComment(models.Model):
    """Модель комментрария к статье хроники"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chronicle_comments', verbose_name='user')
    article = models.ForeignKey(ChronicleArticles, on_delete=models.CASCADE, related_name='comments', verbose_name='chronicle_article')
    text = models.TextField(verbose_name='text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')

    class Meta:
        db_table = 'chronicle_comment'
        verbose_name = 'chronicle_comment'
        verbose_name_plural = 'chronicle_comments'

    def __str__(self):
        return f"Comment for {self.article} by {self.user}"



