from rest_framework import viewsets

from apps.credential.models import (
    BankCard,
    BankDetail,
    WebApplication,
    UPIGateway,
    SecretNote,
    Identity,
)
from apps.credential.serializers import (
    BankCardSerializer,
    BankDetailSerializer,
    WebApplicationSerializer,
    UPIGatewaySerializer,
    SecretNoteSerializer,
    IdentitySerializer,
)


class CredentialMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(owned_by=self.request.user)
        return queryset


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
