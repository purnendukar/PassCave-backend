from rest_framework import urlpatterns
from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.user.apis import UserProfileViewSet


default_router = DefaultRouter(trailing_slash=False)

default_router.register("", UserProfileViewSet, basename="user")

urlpatterns = [
    path(
        "",
        UserProfileViewSet.as_view(
            {"get": "retrieve", "post": "create", "patch": "partial_update"}
        ),
        name="user",
    )
] + default_router.urls
