from unicodedata import category

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=76)
    def __str__(self):
        return f'{self.name}'

class Tag(models.Model):
    name = models.CharField(max_length=76)

class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=156)
    content = models.CharField(max_length=356)
    rate = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    catergory = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'{self.title}, {self.content}'

# Create your models here.