from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from apps.credential.apis import BankCardViewSet, BankDetailViewSet, SecretNoteViewSet, UPIGatewayViewSet, IdentityViewSet, WebApplicationViewSet


default_router = DefaultRouter(trailing_slash=False)

default_router.register("bank_card", BankCardViewSet)
default_router.register("bank_detail", BankDetailViewSet)
default_router.register("upi_gateway", UPIGatewayViewSet)
default_router.register("identity", IdentityViewSet)
default_router.register("web_application", WebApplicationViewSet)
default_router.register("secret_note", SecretNoteViewSet)


urlpatterns = default_router.urls
