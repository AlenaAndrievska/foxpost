import random

from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Articles, Currency, Category, ChronicleCategory, ChronicleArticles
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from .forms import ExtendedRegisterForm, LoginForm, CommentForm, ChronicleCommentForm
import datetime
from .services import CommentsService, ChronicleCommentsService, currency_service


class ArticlesListView(ListView):
    """
    Отображает список новостей
    """
    model = Articles
    context_object_name = 'articles_list'
    paginate_by = 12


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = datetime.datetime.today()
        currency = currency_service(date)
        categories_list = Category.objects.all()
        chronic_categories_list = ChronicleCategory.objects.all()
        photos = Articles.objects.filter(name='photo').order_by("-created_at")
        slug = self.kwargs.get('category_slug', None)
        if slug:
            category_name = categories_list.get(slug=slug)
            context['title'] = getattr(category_name, "name")
        else:
            context['title'] = ''
        context['currency_object'] = currency
        context['categories_list'] = categories_list
        context['photos'] = photos
        context['chronic_categories_list'] = chronic_categories_list
        return context

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Articles.objects.all()
            slug = self.kwargs.get('category_slug', None)
            if slug:
                queryset = queryset.filter(name=slug).order_by("-created_at")
            else:
                queryset = queryset.order_by("-created_at")

            return queryset


class ArticlesDetailView(DetailView):
    """
    Отображает детальную страницу статьи
    """
    model = Articles
    context_object_name = 'article'
    slug_field = 'article_slug'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = CommentsService(
                self.request,
                self.request.user,
                self.get_object().id
            )
            text = form.cleaned_data['text']
            comment.add(text)
            return redirect(request.META.get('HTTP_REFERER'))


    def get_object(self, *args, **kwargs):
        return Articles.objects.get(slug=self.kwargs.get('article_slug'))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_service = CommentsService(self.request, self.request.user, self.object)
        articles_list = Articles.objects.filter(category=getattr(self.object, "category"))
        date = datetime.datetime.today()
        currency = currency_service(date)
        #queryset_count = Articles.objects.filter(name='photo').count()
        #random_indexes = random.sample(range(queryset_count), min(queryset_count, 100))
        photos = Articles.objects.filter(name='photo').order_by("-created_at")
        #.filter(pk__in=random_indexes)
        categories_list = Category.objects.all()
        context['currency_object'] = currency
        context['categories_list'] = categories_list
        context['comments'] = comment_service.get_comments_for_article()
        context['paginator'], context['page_obj'] = comment_service.paginate(context['comments'])
        context['articles_list'] = articles_list
        context['photos'] = photos
        context['comment_form'] = CommentForm()
        return context



def user_login(request):
    date = datetime.datetime.today()
    context = {'currency_object': currency_service(date),
               'categories_list': Category.objects.all()}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        context['form'] = form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect('/articles/', {'username': username, })
            else:
                form.add_error(None, 'Аккаунт не существует. Попробуйте еще раз.')
                return render(request, 'parser_app/login.html', context)
        else:
            return render(request, 'parser_app/login.html', context)
    else:
        form = LoginForm()
        context['form'] = form
        return render(request, 'parser_app/login.html', context)


class LogOutView(LogoutView):
    next_page = '/articles/'


def register_view(request):
    date = datetime.datetime.today()
    context = {'currency_object': currency_service(date),
               'categories_list': Category.objects.all()}
    if request.method == 'POST':
        form = ExtendedRegisterForm(request.POST)
        context['form'] = form
        form = ExtendedRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/articles/')
        else:
            form.add_error(None, 'Вы ввели недопустимое значение.')
            return render(request, 'parser_app/register.html', context)
    else:
        form = ExtendedRegisterForm()
        context['form'] = form

    return render(request, 'parser_app/register.html', context)


class ChronicleCategoryList(ListView):
    """
    Отображает список категорий раздела Хроники
    """
    model = ChronicleCategory
    context_object_name = 'chronic_categories_list'
    template_name = 'parser_app/chronicle_categories_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = datetime.datetime.today()
        currency = currency_service(date)
        categories_list = Category.objects.all()
        context['currency_object'] = currency
        context['categories_list'] = categories_list
        return context


class ChronicleArticlesList(ListView):
    """
    Отображает список новостей из раздела Хроники
    """
    model = ChronicleArticles
    context_object_name = 'chronicle_articles_list'
    template_name = 'parser_app/chronicle_articles_list.html'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = datetime.datetime.today()
        categories_list = Category.objects.all()
        currency = currency_service(date)
        #queryset_count = Articles.objects.filter(name='photo').count()
        #random_indexes = random.sample(range(queryset_count), min(queryset_count, 100))
        photos = Articles.objects.filter(name='photo').order_by("-created_at")
        #.filter(pk__in=random_indexes)
        slug = self.kwargs.get('chronicle_category_slug', None)
        chronicle = ChronicleCategory.objects.get(slug=slug)
        context['categories_list'] = categories_list
        context['currency_object'] = currency
        context['chronicle'] = chronicle
        context['photos'] = photos
        return context

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = ChronicleArticles.objects.all()
            slug = self.kwargs.get('chronicle_category_slug', None)
            if slug:
                queryset = queryset.filter(chronicle_name=slug).order_by("-created_at")
            else:
                queryset = queryset

            return queryset


class ChronicleArticlesDetail(DetailView):
    """
    Отображает детальную страницу статьи
    """
    model = ChronicleArticles
    context_object_name = 'article'
    slug_field = 'chronicle_articles_slug'
    template_name = 'parser_app/chronicle_article_detail.html'

    def post(self, request, *args, **kwargs):
        form = ChronicleCommentForm(request.POST)
        if form.is_valid():
            comment = ChronicleCommentsService(
                self.request,
                self.request.user,
                self.get_object().id
            )
            text = form.cleaned_data['text']
            comment.add(text)
            return redirect(request.META.get('HTTP_REFERER'))


    def get_object(self, *args, **kwargs):
        return ChronicleArticles.objects.get(slug=self.kwargs.get('chronicle_articles_slug'))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles_list = ChronicleArticles.objects.filter(chronicle=getattr(self.object, "chronicle"))
        comment_service = ChronicleCommentsService(self.request, self.request.user, self.object)
        date = datetime.datetime.today()
        currency = currency_service(date)
        #queryset_count = Articles.objects.filter(name='photo').count()
        #random_indexes = random.sample(range(queryset_count), min(queryset_count, 100))
        photos = Articles.objects.filter(name='photo').order_by("-created_at")
        #.filter(pk__in=random_indexes)
        categories_list = Category.objects.all()
        context['currency_object'] = currency
        context['categories_list'] = categories_list
        context['comments'] = comment_service.get_comments_for_article()
        context['articles_list'] = articles_list
        context['photos'] = photos
        context['comment_form'] = ChronicleCommentForm()
        return context








