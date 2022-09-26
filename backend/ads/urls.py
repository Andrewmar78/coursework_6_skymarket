from django.urls import path, include
from rest_framework import routers

from backend.ads.views.ad import AdViewSet
from backend.ads.views.comment import CommentViewSet

router = routers.SimpleRouter()
router.register('ad', AdViewSet)
router.register('ad/?<ad_id>/comments', CommentViewSet, basename='comments')

# urlpatterns += router.urls
urlpatterns = [path('', include(router.urls)), ]
