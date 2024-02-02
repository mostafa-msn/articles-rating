from rest_framework import serializers

from articles.models import Article, Rating


class ArticleSerializer(serializers.ModelSerializer):
    average_score = serializers.SerializerMethodField()
    rated_count = serializers.SerializerMethodField()
    user_rating = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'average_score', 'rated_count', 'user_rating']

    def get_average_score(self, obj):
        return obj.average_rating()

    def get_rated_count(self, obj):
        return obj.rated_count()

    def get_user_rating(self, obj):
        user = self.context['request'].user
        if user.is_authenticated and obj.rating_set.filter(user=user).exists():
            return obj.rating_set.get(user=user).score
        return None


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'article', 'score']

    def create(self, validated_data):
        user = self.context['request'].user
        article = validated_data['article']
        score = validated_data['score']

        rating, created = Rating.objects.update_or_create(
            user=user, article=article, defaults={'score': score})

        # Update average rating in the cache
        article.update_average_rating()

        return rating
