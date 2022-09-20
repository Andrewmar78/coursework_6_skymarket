from django.db import models

from .ad import Ad
from users.models import User


class Comment(models.Model):
    text = models.TextField(blank=True, max_length=5000)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text
