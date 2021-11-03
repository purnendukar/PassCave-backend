from django.db.models import fields
from rest_framework import serializers

from rest_framework.authtoken.models import Token

from apps.user.models import User, UserProfile


class AuthRequestSerializers(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = ["email", "password"]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserAuthSerializers(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["email", "profile", "token"]

    def get_token(self, user):
        token, created = Token.objects.get_or_create(user=user)
        return token.key

    def get_profile(self, instance):
        if hasattr(instance, "profile"):
            return UserProfileSerializer(instance.profile).data
        return None


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]
