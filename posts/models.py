from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    SCORES = (
        (1, 'Ruim'),
        (2, 'Regular'),
        (3, 'Bom'),
        (4, 'Muito Bom'),
        (5, 'Ótimo')
    )
    title = models.CharField(max_length=500, null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=SCORES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=False)


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=500)


class Enrollment(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

class Course(models.Model):
    name = models.CharField(max_length=500)
    users = models.ManyToManyField(User, through=Enrollment)