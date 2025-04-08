from django.contrib import admin
from .models import Articles, Category, Currency, Comment, ChronicleCategory, ChronicleArticles, ChronicleComment



@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'description', 'photo', 'name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


@admin.register(ChronicleCategory)
class ChronicleCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'description', 'photo')


@admin.register(ChronicleArticles)
class ChronicleArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'description', 'photo', 'chronicle_name', 'chronicle')


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'dollar', 'euro', 'dollar_diff', 'euro_diff', 'day')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'article', 'text', 'created_at')


@admin.register(ChronicleComment)
class ChronicleCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'article', 'text', 'created_at')


