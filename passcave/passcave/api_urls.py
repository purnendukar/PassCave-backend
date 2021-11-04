from django.urls import path
from django.urls.conf import include

from rest_framework.routers import DefaultRouter

from apps.user.apis import AuthViewset


default_router = DefaultRouter(trailing_slash=False)

default_router.register("auth", AuthViewset, basename="auth")


urlpatterns = [
    path("credentials/", include("apps.credential.urls"), name="credential"),
    path("plan/", include("apps.plan.urls"), name="plan"),
    path("organisation/", include("apps.organisation.urls"), name="organisation"),
]
urlpatterns += default_router.urls
