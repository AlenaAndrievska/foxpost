import datetime
from typing import Tuple, Any
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.http import HttpRequest
from .models import Comment, Articles, ChronicleArticles, ChronicleComment, Currency

User = get_user_model()


def currency_service(date):
    if Currency.objects.filter(day=date).exists():
        currency = Currency.objects.get(day=date)
    else:
        currency = Currency.objects.get(day=date - datetime.timedelta(days=1))
    return currency


class CommentsService:
    """Сервис для работы с комментариями"""
    def __init__(self, request: HttpRequest, profile: User, article: Articles):
        self.request = request
        self.article = article
        self.profile = profile

    def add(self, comment: str) -> None:
        """
        Добавляет комментарий к статье
        :param comment: текст комментария к статье
        :return: None
        """
        Comment.objects.create(
            user=self.profile,
            article_id=self.article,
            text=comment,
        )


    def get_comments_for_article(self) -> QuerySet[Comment]:
        """
        Возвращает все комментарии к статье
        :return: список комментариев
        """
        comments = Comment.objects.filter(article=self.article).order_by('-created_at')
        return comments

    def paginate(self, comments: QuerySet[Comment]) -> Tuple[Paginator, Any]:
        """
        Возвращает пагинатор для работы пагинации комментариев к статье
        :param comments: список комментариев к статье
        :return: пагинатор и объект пагинации
        """
        paginator = Paginator(comments, 3)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return paginator, page_obj


class ChronicleCommentsService:
    """Сервис для работы с комментариями"""
    def __init__(self, request: HttpRequest, profile: User, article: ChronicleArticles):
        self.request = request
        self.article = article
        self.profile = profile

    def add(self, comment: str) -> None:
        """
        Добавляет комментарий к статье
        :param comment: текст комментария к статье
        :return: None
        """
        ChronicleComment.objects.create(
            user=self.profile,
            article_id=self.article,
            text=comment,
        )


    def get_comments_for_article(self) -> QuerySet[Comment]:
        """
        Возвращает все комментарии к статье
        :return: список комментариев
        """
        comments = ChronicleComment.objects.filter(article=self.article).order_by('-created_at')
        return comments

    def paginate(self, comments: QuerySet[Comment]) -> Tuple[Paginator, Any]:
        """
        Возвращает пагинатор для работы пагинации комментариев к статье
        :param comments: список комментариев к статье
        :return: пагинатор и объект пагинации
        """
        paginator = Paginator(comments, 3)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return paginator, page_obj
