from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Anime(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=360)
    personal_impression = models.TextField(max_length=200)
    release_year = models.IntegerField()
    cover = models.FileField(upload_to='covers/', blank=True)
    link_to_watch = models.URLField(max_length=300)

    def number_of_ratings(self):
        ratings = Rating.objects.filter(anime=self)
        return len(ratings)

    def avg_rating(self):
        sum_ = 0
        ratings = Rating.objects.filter(anime=self)
        for rating in ratings:
            sum_ += rating.stars
        if len(ratings) > 0:
            return sum_ / len(ratings)
        else:
            return 0


class Rating(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        unique_together = (('user', 'anime'), )
        index_together = (('user', 'anime'), )
