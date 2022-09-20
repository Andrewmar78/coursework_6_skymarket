# Доработать
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from backend.ads.models.ad import Ad
from backend.ads.serializers.ad import AdListSerializer, AdRetrieveSerializer, AdCreateSerializer, AdSerializer


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    serializer_action_classes = {
        'list': AdListSerializer,
        'retrieve': AdRetrieveSerializer,
        'create': AdCreateSerializer,
    }
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path=r'me')
    def user_ads(self, request, *args, **kwargs):
        current_user = self.request.user
        queryset = Ad.objects.filter(author=current_user)
        serializer = AdListSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
