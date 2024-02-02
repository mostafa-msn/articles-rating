from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from articles.models import Article
from articles.serializers import ArticleSerializer, RatingSerializer


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_serializer_context(self):
        context = super(ArticleListView, self).get_serializer_context()
        context.update({"request": self.request})
        return context


class RateArticleView(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super(RateArticleView, self).get_serializer_context()
        context.update({"request": self.request})
        return context
