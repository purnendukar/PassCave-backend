from rest_framework.routers import DefaultRouter

from apps.secret_group.apis import SecretGroupViewSet


default_router = DefaultRouter(trailing_slash=False)

default_router.register("", SecretGroupViewSet, basename="secret_group")


urlpatterns = default_router.urls
