from django.db import models


class Spreadsheet(models.Model):
    file = models.CharField(max_length=100)
    path = models.CharField(max_length=300)
    is_merged = models.BooleanField(default=True)
