from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from apps.user.apis import AuthViewset


default_router = DefaultRouter(trailing_slash=False)

urlpatterns = default_router.urls
