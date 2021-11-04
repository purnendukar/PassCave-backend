from django.urls.conf import path

from rest_framework.routers import DefaultRouter

from apps.secret_group.apis import SecretGroupViewSet


default_router = DefaultRouter(trailing_slash=False)


urlpatterns = [
    path(
        "",
        SecretGroupViewSet.as_view(
            {"get": "retrieve", "post": "create", "patch": "partial_update"}
        ),
        name="secret_group",
    )
]
