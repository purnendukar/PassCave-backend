from django.db.models import fields
from rest_framework import serializers

from apps.credential.models import (
    BankCard,
    BankDetail,
    WebApplication,
    UPIGateway,
    SecretNote,
    Identity,
)
from apps.user.serializers import UserSerializers


class BaseSerializer(serializers.Serializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["owned_by"] = UserSerializers(instance.owned_by).data
        data["access_given"] = UserSerializers(instance.access_given.all()).data
        return data


class BankCardSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = BankCard


class BankDetailSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = BankDetail


class WebApplicationSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = WebApplication


class UPIGatewaySerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = UPIGateway


class SecretNoteSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = SecretNote


class IdentitySerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = Identity
