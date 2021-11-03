from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.base import mixins

from apps.user.models import User
from apps.user.serializers import AuthRequestSerializers, UserAuthSerializers


# Create your views here.
class AuthViewset(mixins.MultiRequestValidatorMixin, viewsets.GenericViewSet):
    model = User
    queryset = model.objects.all()
    # serializer_classes = {
    #     "register": AuthRequestSerializers
    # }
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
            {"message": "Registration successful", "data": serializer.data},
            status.HTTP_201_CREATED,
        )

    @action(methods=["POST"], detail=False, permission_classes=[])
    def login(self, request):
        data, context = self.request_valiator()
        user = authenticate(**data)
        serializer = self.get_serializer(user, context=context)
        return Response({"message": "Login successful", "data": serializer.data})

    @action(methods=["POST"], detail=False, permission_classes=[])
    def logout(self, request):
        request.auth.delete()
        return Response({"message": "Logout Succcessful"})
