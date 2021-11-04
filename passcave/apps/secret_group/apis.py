from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins

from apps.secret_group.models import SecretGroup
from apps.secret_group.serializers import SecretGroupSerializer


class SecretGroupViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = SecretGroup.objects.all()
    serializer_class = SecretGroupSerializer

    def get_queryset(self):
        return super().get_queryset().filter(admin=self.request.user)

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {"admin": self.request.user.id}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

    def create(self, request, *args, **kwargs):
        request.data["admin"] = request.user.id
        return super().create(request, *args, **kwargs)
