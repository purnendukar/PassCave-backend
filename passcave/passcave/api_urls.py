from django.urls import path
from django.urls.conf import include

from rest_framework.routers import DefaultRouter

from apps.user.apis import AuthViewset


default_router = DefaultRouter(trailing_slash=False)

default_router.register("auth", AuthViewset, basename="auth")


urlpatterns = [
    path("secrets/", include("apps.secrets.urls"), name="secrets"),
    path("plan/", include("apps.plan.urls"), name="plan"),
    path("secret_group", include("apps.secret_group.urls"), name="secret_group"),
    path("me/", include("apps.user.urls"), name="me"),
]
urlpatterns += default_router.urls
