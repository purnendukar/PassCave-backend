from django.db.models import fields
from rest_framework import serializers

from rest_framework.authtoken.models import Token

from apps.user.models import User, UserProfile
from apps.plan.serializers import PlanSerializer


class AuthRequestSerializers(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = ["email", "password"]


class UserProfileResponseSerializer(serializers.ModelSerializer):
    plan = PlanSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ["plan"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["user", "plan"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["plan"] = PlanSerializer(instance.plan).data
        return data


class UserAuthSerializers(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    profile = UserProfileResponseSerializer(read_only=True, many=False)

    class Meta:
        model = User
        fields = ["email", "profile", "token"]

    def get_token(self, user):
        token, created = Token.objects.get_or_create(user=user)
        return token.key


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]


class UserProfileSerializer(UserSerializer):
    profile = UserProfileResponseSerializer(read_only=True, many=False)

    class Meta:
        model = User
        fields = UserSerializer.Meta.fields + ["profile"]


class UserPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["plan"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["plan"] = PlanSerializer(instance.plan).data
        return data
