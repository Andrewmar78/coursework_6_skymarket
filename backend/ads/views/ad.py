from rest_framework.decorators import action
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from backend.ads.models.ad import Ad
from backend.ads.serializers import AdListSerializer, AdCreateSerializer, AdDestroySerializer

# Доработать
class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer

    serializer_classes = {
        'list': AdListSerializer,
        'get': AdListSerializer,
        'retrieve': AdRetrieveSerializer,
        'create': AdCreateSerializer,
        'update': AdUpdateSerializer,
    }
    permission_classes = UserPermissions

    @action(detail=False, methods=['get'], serializer_class=AdListSerializer)
    # Подсмотрел в интернете https://django.fun/ru/docs/django-rest-framework/3.12/api-guide/viewsets/
    def user_ads(self, request):
        current_user = self.request.user
        user_ads = Ad.objects.filter(author=current_user)

        page = self.paginate_queryset(user_ads)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(current_user, many=True)
        return Response(serializer.data)

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
    #
    # def get_serializer_class(self):
    #     try:
    #         return self.serializer_action_classes[self.action]
    #     except (KeyError, AttributeError):
    #         return super().get_serializer_class()

# class AdDeleteView(DestroyAPIView):
#     queryset = Ad.objects.all()
#     serializer_class = AdDestroySerializer
