from django.db import models

# Create your models here.

class Search(models.Model):
    keyword = models.CharField(max_length=500, blank=True,null=True)
    cv_data = models.CharField(max_length=500, blank=True,null=True)

    def __str__(self):
        return self.keyword
