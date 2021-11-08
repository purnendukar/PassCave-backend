from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from apps.base import mixins as base_mixins
from apps.user.models import User, UserProfile
from apps.user.serializers import (
    AuthRequestSerializers,
    UserAuthSerializers,
    ProfileSerializer,
    UserProfileSerializer,
    UserSerializer,
)


# Create your views here.
class AuthViewset(base_mixins.MultiRequestValidatorMixin, viewsets.GenericViewSet):
    model = User
    queryset = model.objects.all()
    serializer_class = UserAuthSerializers
    request_serializer_classes = {
        "signup": AuthRequestSerializers,
        "login": AuthRequestSerializers,
    }

    @action(methods=["POST"], detail=False, permission_classes=[])
    def signup(self, request):
        data, context = self.request_valiator()
        user = self.model.objects.create_user(**data)
        serializer = self.get_serializer(user, context=context)
        return Response(
            serializer.data,
            status.HTTP_201_CREATED,
        )

    @action(methods=["POST"], detail=False, permission_classes=[])
    def login(self, request):
        data, context = self.request_valiator()
        user = authenticate(**data)
        serializer = self.get_serializer(user, context=context)
        return Response(serializer.data)

    @action(methods=["POST"], detail=False)
    def logout(self, request):
        request.auth.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserProfileViewSet(
    base_mixins.MultiSerializerMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ProfileSerializer
    serializer_classes = {
        "retrieve": UserProfileSerializer,
        "partial_update": UserProfileSerializer,
    }

    def get_object(self):
        return self.request.user

    def create(self, request, *args, **kwargs):
        request.data["user"] = str(request.user.id)
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        user_data = request.data.copy()

        if user_data.get("profile"):
            del user_data["profile"]

        user_serializer = UserSerializer(request.user, data=user_data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        serializer = self.get_serializer(
            instance, data=request.data.get("profile", {}), partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
