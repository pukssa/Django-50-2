from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=156)
    content = models.CharField(max_length=356)
    rate = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.title}, {self.content}'

# Create your models here.