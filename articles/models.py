from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg

from lib.common_model import BaseModel


class Article(BaseModel):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def update_average_and_count(self):
        key_avg = f'article_{self.id}_avg_rating'
        key_count = f'article_{self.id}_rated_count'

        avg_rating = self.rating_set.aggregate(avg_rating=Avg('score')).get('avg_rating') or 0
        rated_count = self.rating_set.count()

        cache.set(key_avg, avg_rating)
        cache.set(key_count, rated_count)

        return avg_rating, rated_count

    @property
    def average_rating(self):
        key_avg = f'article_{self.id}_avg_rating'
        avg_rating = cache.get(key_avg)
        if avg_rating is None:
            avg_rating, _ = self.update_average_and_count()
        return avg_rating

    @property
    def rated_count(self):
        key_count = f'article_{self.id}_rated_count'
        rated_count = cache.get(key_count)
        if rated_count is None:
            _, rated_count = self.update_average_and_count()
        return rated_count


class Rating(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
