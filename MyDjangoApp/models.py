from django.db import models


class Topic(models.Model):
    topName = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.topName


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=True)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=True)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class User(models.Model):
    fname = models.CharField(max_length=264)
    lname = models.CharField(max_length=264)
    email = models.EmailField(max_length=264,unique=True)

    def __str__(self):
        return str(self.fname) + " " + str(self.lname)

