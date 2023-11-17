import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Todo(models.Model):
    text = models.TextField()
    expires_at = models.DateTimeField(default=datetime.datetime.now())
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


