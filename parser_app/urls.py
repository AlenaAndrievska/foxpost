from django.urls import path
from .models import Articles
from .views import ArticlesListView, ArticlesDetailView,  LogOutView, register_view, user_login,\
    ChronicleCategoryList, ChronicleArticlesList, ChronicleArticlesDetail

app_name = 'article'

urlpatterns = [
    path('', ArticlesListView.as_view(queryset=Articles.objects.all().order_by("-created_at"))),
    path('articles/', ArticlesListView.as_view(queryset=Articles.objects.all().order_by("-created_at"))),
    path('articles/chronicle/', ChronicleCategoryList.as_view(), name='chronicle_categories_list'),
    path('articles/story/', ChronicleCategoryList.as_view(), name='chronicle_categories_list'),
    path('articles/chronicle/<slug:chronicle_category_slug>/', ChronicleArticlesList.as_view(),
         name='chronicle_articles_list'),
    path('articles/<slug:category_slug>/', ArticlesListView.as_view(), name='articles_list'),
    path('articles/chronicle/<slug:chronicle_category_slug>/<slug:chronicle_articles_slug>/',
         ChronicleArticlesDetail.as_view(), name='chronicle_article_detail'),
    path('articles/<slug:category_slug>/<slug:article_slug>/', ArticlesDetailView.as_view(), name='articles_detail'),
    path('login/', user_login, name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
]
