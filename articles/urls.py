from django.urls import path
from .views import ArticleListView, RateArticleView

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='article-list'),
    path('rate-article/', RateArticleView.as_view(), name='rate-article'),
]