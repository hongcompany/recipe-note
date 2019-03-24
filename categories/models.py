from django.db import models


# Create your models here.
from django.utils.datetime_safe import datetime


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now())
    is_deleted = models.BooleanField(default=False)
    owner = models.CharField(max_length=200)  # 추후 user 로 변경

    def __str__(self):
        return "name: %s, created_at: %s. owner: %s" % (self.name, self.created_at, self.owner)
