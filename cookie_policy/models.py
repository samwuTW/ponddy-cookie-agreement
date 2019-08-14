from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class AcceptRecord(models.Model):
    ip = models.CharField(max_length=40)  # IPv6 with 39 char
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ip} {self.datetime}'
