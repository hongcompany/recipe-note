from django.db import models


# Create your models here.
from django.utils.datetime_safe import datetime


class Category(models.Model):
    name = models.CharField(max_length=200)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # owner = models.CharField(max_length=200)  # 추후 user 로 변경
