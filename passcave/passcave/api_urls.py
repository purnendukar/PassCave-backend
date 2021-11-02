from django.urls import path
from django.urls.conf import include


urlpatterns = [path("credential/", include("apps.credential.urls"), name="credential")]
