from django.db import models

# Create your models here.

class movieId(models.Model):
    movieId=models.ImageField()
    titles=models.CharField(max_length=500)
    geners=models.CharField(max_length=1000)
    class Meta:
        db_table = "movie"


class emp(models.Model):
    Name=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    salary=models.IntegerField()
    status=models.BooleanField()
    class Meta:
        db_table = "Emp"
