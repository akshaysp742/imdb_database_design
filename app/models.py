from django.db import models
from django.contrib.auth.models import User


class StreamingPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    website = models.URLField()

    def __str__(self):
        return self.name


class ActorsDetails(models.Model):
    name = models.CharField(max_length=50)
    contact_info = models.TextField()

    def __str__(self):
        return self.name


class Generes(models.Model):
    genere = models.CharField(max_length=50)

    def __str__(self):
        return self.genere


class TechnicalSpecs(models.Model):
    runtime = models.FloatField()
    colour = models.CharField(max_length=20)


class Directors(models.Model):
    name = models.CharField(max_length=50)
    contact_details = models.TextField()

    def __str__(self):
        return self.name


class Writers(models.Model):
    name = models.CharField(max_length=50)
    contact_details = models.TextField()

    def __str__(self):
        return self.name


# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.TextField()
    release_date = models.DateField
    country_of_origin = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    production_house = models.CharField(max_length=50)
    platform = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE)
    cast = models.ManyToManyField(ActorsDetails)
    movie_genere = models.ManyToManyField(Generes)
    movie_director = models.ManyToManyField(Directors)
    movie_writer = models.ManyToManyField(Writers)
    movie_specs = models.ManyToManyField(TechnicalSpecs)

    def __str__(self):
        return self.title


class Reviews(models.Model):
    rating = models.PositiveIntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ForeignKey(Movies, on_delete=models.CASCADE)
