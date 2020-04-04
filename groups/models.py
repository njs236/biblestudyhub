from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="group/", blank=True)
    public = models.BooleanField(default=True)


class StudySession(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="group/", blank=True)
    date = models.DateTimeField(blank=True, null=True)
    meeting_link = models.CharField(max_length=300)
    public = models.BooleanField(default=True)


