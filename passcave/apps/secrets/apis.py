from rest_framework import mixins, viewsets

from apps.secrets.models import (
    BankCard,
    BankDetail,
    WebApplication,
    UPIGateway,
    SecretNote,
    Identity,
    Secret,
)
from apps.secrets.serializers import (
    BankCardSerializer,
    BankDetailSerializer,
    WebApplicationSerializer,
    UPIGatewaySerializer,
    SecretNoteSerializer,
    IdentitySerializer,
    SecretSerializer,
)


class CredentialMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(owned_by=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        request.data["owned_by"] = request.user.id
        return super().create(request, *args, **kwargs)


class SecretViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Secret.objects.all()
    serializer_class = IdentitySerializer


class BankCardViewSet(CredentialMixin, viewsets.ModelViewSet):
    queryset = BankCard.objects.all()
    serializer_class = BankCardSerializer


class BankDetailViewSet(CredentialMixin, viewsets.ModelViewSet):
    queryset = BankDetail.objects.all()
    serializer_class = BankDetailSerializer


class WebApplicationViewSet(CredentialMixin, viewsets.ModelViewSet):
    queryset = WebApplication.objects.all()
    serializer_class = WebApplicationSerializer


class UPIGatewayViewSet(CredentialMixin, viewsets.ModelViewSet):
    queryset = UPIGateway.objects.all()
    serializer_class = UPIGatewaySerializer


class SecretNoteViewSet(CredentialMixin, viewsets.ModelViewSet):
    queryset = SecretNote.objects.all()
    serializer_class = SecretNoteSerializer


class IdentityViewSet(CredentialMixin, viewsets.ModelViewSet):
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializer
