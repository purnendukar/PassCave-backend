from rest_framework import viewsets

from apps.credential.models import Credential
from apps.credential.serializers import CredentialSerializer


class CredentialViewset(viewsets.ModelViewSet):
    queryset = Credential
    serializer_class = CredentialSerializer
