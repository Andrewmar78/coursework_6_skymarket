from django.contrib import admin

from .models.ad import Ad
from .models.comment import Comment

admin.site.register(Ad)
admin.site.register(Comment)
