from rest_framework import serializers

from rest_framework.authtoken.models import Token

from apps.user.models import User, UserProfile
from apps.plan.serializers import PlanSerializer


class AuthRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class SignRequestSerializer(AuthRequestSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()
    new_password = serializers.CharField()

    class Meta:
        fields = ["email", "token", "new_password"]


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


class UserAuthSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    profile = UserProfileResponseSerializer(read_only=True, many=False)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "profile", "token"]

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
        read_only_fields = ["email"]


class UserPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["plan"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["plan"] = PlanSerializer(instance.plan).data
        return data
