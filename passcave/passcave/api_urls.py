from django.urls import path
from django.urls.conf import include

from rest_framework.routers import DefaultRouter

from apps.user.apis import AuthViewset


default_router = DefaultRouter(trailing_slash=False)

default_router.register("auth", AuthViewset, basename="auth")


urlpatterns = [path("credential/", include("apps.credential.urls"), name="credential")]
urlpatterns += default_router.urls
