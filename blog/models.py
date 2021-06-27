from django.db import models

class Blogg(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=500)
    mydatetime=models.DateTimeField()
