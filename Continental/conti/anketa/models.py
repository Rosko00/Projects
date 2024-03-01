from django.db import models

class Message(models.Model):
    text = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
