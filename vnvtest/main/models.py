from django.db import models


class Group(models.Model):
    name = models.CharField('name', max_length=255)
    description = models.TextField('description')

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField('username', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    group = models.CharField('group', max_length=255)

    def __str__(self):
        return self.username

