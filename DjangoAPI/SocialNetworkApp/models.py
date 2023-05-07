from django.db import models

# Create your models here.

class Test(models.Model):
    TestId = models.AutoField(primary_key=True)
    TestName = models.CharField(max_length=400)