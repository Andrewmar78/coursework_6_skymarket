from rest_framework.viewsets import ModelViewSet
from ads.models.ad import Ad
from ads.models.comment import Comment
from ads.permissions import UserPermissions
from ads.serializers.comment import CommentSerializer, CommentListSerializer, CommentCreateSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    serializer_action_classes = {
        'list': CommentListSerializer,
        'retrieve': CommentListSerializer,
        'create': CommentCreateSerializer,
        'update': CommentCreateSerializer,
    }

    permission_classes = [UserPermissions]

    def get_queryset(self):
        return Comment.objects.filter(ad_id=self.kwargs['ad_id'])

    def get_serializer_class(self):
        return self.serializer_action_classes.get(self.action)

    def perform_create(self, serializer):
        ad = Ad.objects.get(pk=self.kwargs['ad_id'])
        serializer.save(author=self.request.user, ad=ad)
