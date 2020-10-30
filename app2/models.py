from django.db import models
#from django_pandas.io import read_frame


class movieId(models.Model):
    movieId=models.IntegerField()
    title=models.CharField(max_length=500)
    genres=models.CharField(max_length=1000)
    class Meta:
        db_table = "movie"
# Create your models here.
class emp(models.Model):
    Name=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    salary=models.IntegerField()
    status=models.BooleanField()
    class Meta:
        db_table = "Emp"

class Ratings(models.Model):
    userId=models.IntegerField()
    movieId=models.IntegerField()
    rating=models.BooleanField()
    timestamp=models.IntegerField()
    class Meta:
        db_table="ratings"
