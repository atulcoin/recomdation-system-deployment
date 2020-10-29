from django.db import models


class movieId(models.Model):
    movieId=models.ImageField()
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
