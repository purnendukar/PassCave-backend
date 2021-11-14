from rest_framework.routers import DefaultRouter

from apps.secrets.apis import (
    BankCardViewSet,
    BankDetailViewSet,
    SecretNoteViewSet,
    UPIGatewayViewSet,
    IdentityViewSet,
    WebApplicationViewSet,
)


default_router = DefaultRouter(trailing_slash=False)

default_router.register("bank_card", BankCardViewSet, basename="bank_card")
default_router.register("bank_detail", BankDetailViewSet, basename="bank_detail")
default_router.register("upi_gateway", UPIGatewayViewSet, basename="upi_gateway")
default_router.register("identity", IdentityViewSet, basename="identity")
default_router.register(
    "web_application", WebApplicationViewSet, basename="web_application"
)
default_router.register("secret_note", SecretNoteViewSet, basename="secret_note")


urlpatterns = default_router.urls
