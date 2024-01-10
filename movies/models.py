from django.db import models
from django.shortcuts import reverse

# Create your models here.
from django.db import models
from jsonfield import JSONField

# from docutils.utils.math.latex2mathml import mo
# managed = False


class AdLinks(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    active = models.BooleanField(default=False, null=True)
    company_name = models.CharField(max_length=500, null=True, blank=True)
    link_name = models.CharField(max_length=500, null=True, blank=True)
    link_address = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.link_name

class BlockedMovies(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=10000, null=True, blank=True)
    def __str__(self):
        return self.title
    

class PopularMovies(models.Model):
    id = models.IntegerField(primary_key=True)
    adult = models.BooleanField(default=False, null=True)
    backdrop_path = models.CharField(max_length=500, null=True, blank=True)
    genre_ids = models.CharField(max_length=10000, null=True, blank=True)
    original_language = models.CharField(max_length=10000, null=True, blank=True)
    original_title = models.CharField(max_length=10000, null=True, blank=True)
    overview = models.CharField(max_length=10000, null=True, blank=True)
    popularity = models.DecimalField(max_digits=100, decimal_places=2)
    poster_path = models.CharField(max_length=10000, null=True, blank=True)
    release_date = models.DateField()
    title = models.CharField(max_length=10000, null=True, blank=True)
    video = models.BooleanField(default=False, null=True)
    vote_average = models.DecimalField(max_digits=100, decimal_places=2)
    vote_count = models.IntegerField(null=True)
    movie_category = models.CharField(max_length=500, null=True, blank=True)
    movie_trailer = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("model_detail", args={self.id})

    def get_absolute_url(self):
        return f"/movie_detail/{self.id}/{self.title}"


class Movies(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)
    premium = models.BooleanField(default=False)
    discription = models.TextField(max_length=10000, null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    thumbnail_link = models.CharField(max_length=1000, null=True, blank=True)
    background_image_link = models.CharField(max_length=1000, null=True, blank=True)
    screen_shot = models.ImageField(upload_to="screenshots/", null=True, blank=True)
    screen_shot_link = models.CharField(max_length=1000, null=True, blank=True)
    movie_length = models.CharField(max_length=50, null=True, blank=True)
    release_date = models.CharField(max_length=100, null=True, blank=True)
    movie_rate = models.CharField(max_length=100, null=True, blank=True)
    imdb_rating = models.CharField(max_length=100, null=True, blank=True)
    movie_director = models.CharField(max_length=200, null=True, blank=True)
    movie_actor = models.CharField(max_length=1000, null=True, blank=True)
    movie_language = models.CharField(max_length=100, null=True, blank=True)
    movie_subtitle = models.CharField(max_length=100, null=True, blank=True)
    movie_type = models.CharField(max_length=200, null=True, blank=True)
    movie_category = models.CharField(max_length=100, null=True, blank=True)
    link_4k = models.CharField(max_length=1000, null=True, blank=True)
    link_1920 = models.CharField(max_length=1000, null=True, blank=True)
    link_720 = models.CharField(max_length=1000, null=True, blank=True)
    size_4k = models.CharField(max_length=1000, null=True, blank=True)
    size_1920 = models.CharField(max_length=1000, null=True, blank=True)
    size_720 = models.CharField(max_length=1000, null=True, blank=True)
    movie_link = models.TextField(max_length=10000, null=True, blank=True)
    movie_online = models.TextField(max_length=1000, null=True, blank=True)
    torent_link_4k = models.CharField(max_length=1000, null=True, blank=True)
    torent_link_1920 = models.CharField(max_length=1000, null=True, blank=True)
    torent_link_720 = models.CharField(max_length=1000, null=True, blank=True)
    torent_file_link = models.FileField(upload_to="torent_movie", null=True, blank=True)
    tmvdbid = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

    def snippet(self):
        return self.discription[:10] + "..."


class NewTrailer(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    link = models.CharField(max_length=1500, null=True, blank=True)
    discription = models.TextField(max_length=5000, null=True, blank=True)
    image = models.ImageField(upload_to="trailer_image", null=True, blank=True)
    image_link = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    def snipet(self):
        return self.discription[:70] + "..."


class SeriesModel(models.Model):
    name = models.CharField(max_length=500)
    discription = models.TextField(max_length=10000, null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    screen_shot = models.ImageField(upload_to="screenshots/", null=True, blank=True)
    series_length = models.CharField(max_length=50, null=True, blank=True)
    release_date = models.DateField()
    series_rate = models.CharField(max_length=100, null=True, blank=True)
    imdb_rating = models.CharField(max_length=100, null=True, blank=True)
    series_director = models.CharField(max_length=200, null=True, blank=True)
    series_actor = models.CharField(max_length=1000, null=True, blank=True)
    series_language = models.CharField(max_length=100, null=True, blank=True)
    series_quality = models.CharField(max_length=100, null=True, blank=True)
    series_size = models.CharField(max_length=100, null=True, blank=True)
    series_subtitle = models.CharField(max_length=100, null=True, blank=True)
    series_type = models.CharField(max_length=200, null=True, blank=True)
    series_subscription = models.CharField(max_length=700, null=True, blank=True)
    series_category = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField()
    seasons = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

    def snipet(self):
        return self.discription[:100] + "..."


class season(models.Model):
    selected_season = models.IntegerField(null=True, blank=True)
    episode = models.IntegerField(null=True, blank=True)
    series = models.OneToOneField(
        SeriesModel, on_delete=models.CASCADE, primary_key=True
    )
    image = models.ImageField(upload_to="seasons/", null=True, blank=True)
    trailer = models.CharField(max_length=5000, null=True, blank=True)
    link1 = models.CharField(max_length=5000, null=True, blank=True)
    link2 = models.CharField(max_length=5000, null=True, blank=True)
    link3 = models.CharField(max_length=5000, null=True, blank=True)
    online_link = models.CharField(max_length=5000, null=True, blank=True)
    id = models.IntegerField(null=True, blank=True)
