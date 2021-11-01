from django.db.models import fields
from rest_framework import serializers

from apps.credential.models import Credential


class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = ["id", "cred_type", "owned_by", "owned_by", "access_given", "detail"]

