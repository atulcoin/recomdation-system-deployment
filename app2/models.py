from django.db import models

# Create your models here.
class emp(models.Model):
    Name=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    salary=models.IntegerField()
    status=models.BooleanField()
    class Meta:
        db_table = "Emp"
