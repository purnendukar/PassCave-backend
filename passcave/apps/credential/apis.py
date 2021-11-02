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


class BankCardViewSet(viewsets.ModelViewSet):
    queryset = BankCard.objects.all()
    serializer_class = BankCardSerializer


class BankDetailViewSet(viewsets.ModelViewSet):
    queryset = BankDetail.objects.all()
    serializer_class = BankDetailSerializer


class WebApplicationViewSet(viewsets.ModelViewSet):
    queryset = WebApplication.objects.all()
    serializer_class = WebApplicationSerializer


class UPIGatewayViewSet(viewsets.ModelViewSet):
    queryset = UPIGateway.objects.all()
    serializer_class = UPIGatewaySerializer


class SecretNoteViewSet(viewsets.ModelViewSet):
    queryset = SecretNote.objects.all()
    serializer_class = SecretNoteSerializer


class IdentityViewSet(viewsets.ModelViewSet):
    queryset = BankDetail.objects.all()
    serializer_class = IdentitySerializer
