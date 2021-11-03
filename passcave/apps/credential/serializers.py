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
        fields = "__all__"


class BankDetailSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = BankDetail
        fields = "__all__"


class WebApplicationSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = WebApplication
        fields = "__all__"


class UPIGatewaySerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = UPIGateway
        fields = "__all__"


class SecretNoteSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = SecretNote
        fields = "__all__"


class IdentitySerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = Identity
        fields = "__all__"
