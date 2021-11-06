from django.db.models import fields
from rest_framework import serializers

from apps.secret_group.models import SecretGroup


class SecretGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretGroup
        fields = ["grp_type", "members"]
