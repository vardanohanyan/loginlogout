from django.db import models

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return f"{self.title}, {self.description[:10]}"

