from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.user.apis import UserViewSet


default_router = DefaultRouter(trailing_slash=False)


default_router.register("", UserViewSet, basename="users")


urlpatterns = default_router.urls
