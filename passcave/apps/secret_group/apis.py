from rest_framework import viewsets
from rest_framework import mixins

from apps.secret_group.models import SecretGroup
from apps.secret_group.serializers import SecretGroupSerializer


class SecretGroupViewSet(
    viewsets.ModelViewSet
):
    queryset = SecretGroup.objects.all()
    serializer_class = SecretGroupSerializer

    def get_queryset(self):
        return super().get_queryset().filter(admin=self.request.user)

    def get_object(self):
        return self.get_queryset().first()

    def perform_create(self, serializer):
        self.request.data["admin"] = self.request.user.id
        return super().perform_create(serializer)
    

