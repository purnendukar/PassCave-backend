from rest_framework import viewsets
from rest_framework import mixins

from apps.organisation.models import Organisation
from apps.organisation.serializers import OrganisationSerializer


class OrganisationViewSet(
    viewsets.ModelViewSet
):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

    def get_queryset(self):
        return super().get_queryset().filter(admin=self.request.user)

    def get_object(self):
        return self.get_queryset().first()

    def perform_create(self, serializer):
        self.request.data["admin"] = self.request.user.id
        return super().perform_create(serializer)
    

