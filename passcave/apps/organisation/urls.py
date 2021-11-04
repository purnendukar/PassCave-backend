from rest_framework.routers import DefaultRouter

from apps.organisation.apis import OrganisationViewSet


default_router = DefaultRouter(trailing_slash=False)

default_router.register("", OrganisationViewSet, basename="organisations")


urlpatterns = default_router.urls
