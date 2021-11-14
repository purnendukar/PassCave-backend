from encrypted_fields import fields
from rest_framework import serializers

from apps.secrets.models import (
    BankCard,
    BankDetail,
    WebApplication,
    UPIGateway,
    SecretNote,
    Identity,
    Secret,
)
from apps.user.serializers import UserSerializer


class BaseSerializer(serializers.Serializer):
    title = serializers.SerializerMethodField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance:
            data["owned_by"] = UserSerializer(instance.owned_by).data
            data["access_given"] = UserSerializer(
                instance.access_given.all(), many=True
            ).data
        return data

    class Meta:
        fields = ["owned_by", "access_given", "title"]

    def get_title(self, obj):
        return obj.secret.all().first().title


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
        fields = [
            "id",
            "url",
            "username",
            "email",
            "mobile",
            "password",
        ] + BaseSerializer.Meta.fields


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


class SecretSerializer(serializers.ModelSerializer):
    _model_serializers = {
        "webapplication": WebApplicationSerializer,
        "bankdetail": BankDetailSerializer,
        "bankcard": BankCardSerializer,
        "identity": IdentitySerializer,
        "secretnote": SecretNoteSerializer,
        "upigateway": UPIGatewaySerializer,
    }

    secret_type = serializers.SerializerMethodField()
    secret_object = serializers.SerializerMethodField()

    class Meta:
        model = Secret
        fields = ["secret_type", "secret_object"]

    def get_secret_type(self, obj):
        return obj.secret_type.model

    def get_secret_object(self, obj):
        serializer = self._model_serializers[obj.secret_type.model](obj.secret_object)
        return serializer.data
