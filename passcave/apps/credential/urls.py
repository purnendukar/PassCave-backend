from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from apps.credential.apis import BankCardViewSet


default_router = DefaultRouter(trailing_slash=False)

default_router.register("bank_card", BankCardViewSet)


urlpatterns = default_router.urls
