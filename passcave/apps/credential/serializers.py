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
from apps.user.serializers import UserSerializer


class BaseSerializer(serializers.Serializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance:
            data["owned_by"] = UserSerializer(instance.owned_by).data
            data["access_given"] = UserSerializer(
                instance.access_given.all(), many=True
            ).data
        return data


class BankCardSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = BankCard
        fields = ["id", "card_number", "expire_month", "expire_year", "cvv", "holder_name", "bank", "card_type"]


class BankDetailSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = BankDetail
        fields = ["id", "account_number", "ifsc_code", "branch_code", "branch_name", "holder_name", "bank"]


class WebApplicationSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = WebApplication
        fields = ["id", "url", "username", "email", "mobile", "password"]


class UPIGatewaySerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = UPIGateway
        fields = ["upi_id", "portal", "pin"]


class SecretNoteSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = SecretNote
        fields = ["id", "topic", "note"]


class IdentitySerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = Identity
        fields = ["id", "id_name", "id_number", "image"]
