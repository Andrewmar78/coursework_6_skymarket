from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(blank=False, max_length=50)
    price = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(blank=True, max_length=5000)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="ads_images/", null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title
