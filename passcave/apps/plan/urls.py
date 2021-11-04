from rest_framework.routers import DefaultRouter

from apps.plan.apis import PlanViewSet


default_router = DefaultRouter(trailing_slash=False)

default_router.register("", PlanViewSet, basename="plans")


urlpatterns = default_router.urls
