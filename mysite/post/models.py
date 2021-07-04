from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
