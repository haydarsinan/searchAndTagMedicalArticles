from django.db import models


# Create your models here.

class articles(models.Model):
    pubmedID = models.TextField()
    title = models.TextField()
    pubDate = models.DateField()
    abstract = models.TextField()
    doi = models.URLField()
    keywords = models.TextField()
    authors = models.TextField()
    tags = models.TextField()

    def __str__(self):
        return self.title


class authors(models.Model):
    name = models.TextField()
    surname = models.TextField(default="SURNAME")

    def __str__(self):
        return self.name + self.surname
