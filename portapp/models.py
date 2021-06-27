from django.db import models

class Port(models.Model):
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=100)
    image= models.ImageField(upload_to="portapp/imagess")
    url=models.URLField(blank=True)

    def __str__(self):
        return self.title
