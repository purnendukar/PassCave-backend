from rest_framework import viewsets
from rest_framework import mixins

from apps.plan.models import Plan
from apps.plan.serializers import PlanSerializer


class PlanViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = []
