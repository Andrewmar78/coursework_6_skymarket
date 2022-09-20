# Доработать
from django.urls import path, include

from views import AdViewSet, CommentViewSet
from rest_framework import routers

ads_router = routers.SimpleRouter()
ads_router.register('ad', AdViewSet)
ads_router.register('ad/(?P<ad_id>[^/.]+)/comments', CommentViewSet, basename='comments')

urlpatterns += ads_router.urls
# urlpatterns = [
#     path('', include(ads_router.urls)),
# ]
