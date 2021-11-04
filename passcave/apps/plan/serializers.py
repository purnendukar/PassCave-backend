from django.db.models import fields
from rest_framework import serializers

from apps.plan.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"