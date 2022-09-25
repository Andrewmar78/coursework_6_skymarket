# Доработать
from django.urls import path, include

from ads.views import AdViewSet, CommentViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('ad', AdViewSet)
router.register('ad/?<ad_id>/comments', CommentViewSet, basename='comments')

# urlpatterns += router.urls
urlpatterns = [path('', include(router.urls)), ]
