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
    
    class Meta:
        fields = ["owned_by", "access_given"]


class BankCardSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = BankCard
        fields = [
            "id",
            "card_number",
            "expire_month",
            "expire_year",
            "cvv",
            "holder_name",
            "bank",
            "card_type",
        ] + BaseSerializer.Meta.fields


class BankDetailSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = BankDetail
        fields = [
            "id",
            "account_number",
            "ifsc_code",
            "branch_code",
            "branch_name",
            "holder_name",
            "bank",
        ] + BaseSerializer.Meta.fields


class WebApplicationSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = WebApplication
        fields = ["id", "url", "username", "email", "mobile", "password"] + BaseSerializer.Meta.fields


class UPIGatewaySerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = UPIGateway
        fields = ["upi_id", "portal", "pin"] + BaseSerializer.Meta.fields


class SecretNoteSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = SecretNote
        fields = ["id", "topic", "note"] + BaseSerializer.Meta.fields


class IdentitySerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = Identity
        fields = ["id", "id_name", "id_number", "image"] + BaseSerializer.Meta.fields
