from django.db.models import fields
from rest_framework import serializers

from apps.organisation.models import Organisation


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = "__all__"
