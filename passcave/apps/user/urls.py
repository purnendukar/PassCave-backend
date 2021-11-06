from rest_framework import urlpatterns
from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.user.apis import UserProfileViewSet


default_router = DefaultRouter(trailing_slash=False)

default_router.register("", UserProfileViewSet)

urlpatterns = [
    path(
        "",
        UserProfileViewSet.as_view({"get": "retrieve"}),
        name="user",
    )
] + default_router.urls
