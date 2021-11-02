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
    UPIGatewayerializer,
    SecretNoteSerializer,
    IdentitySerializer,
)


class BankCardViewSet(viewsets.ModelViewSet):
    queryset = BankCard.objects.all()
    serializer_class = BankCardSerializer
