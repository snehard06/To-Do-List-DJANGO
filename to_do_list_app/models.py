
from django.db import models


class To_Do_List(models.Model):

    title = models.CharField(max_length=20)

    description = models.TextField(max_length=30)

    done = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
