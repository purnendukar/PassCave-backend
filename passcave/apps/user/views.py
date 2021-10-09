from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.base import mixins

from apps.user.models import User
from apps.user.serializers import AuthRequestSerializers, UserAuthSerializers


# Create your views here.
class AuthViewMixin(mixins.MultiRequestValidatorViewMixin, mixins.MultiSerializerViewMixin):
    pass


class AuthViewset(mixins.MultiRequestValidatorViewMixin, viewsets.GenericViewSet):
    model = User
    queryset = model.objects.all()
    # serializer_classes = {
    #     "register": AuthRequestSerializers
    # }
    serializer_class = UserAuthSerializers
    request_serializer_classes = {
        "register": AuthRequestSerializers,
        "login": AuthRequestSerializers
    }

    @action(methods=["POST"], permission_classes=[])
    def register(self, request):
        data,context = self.request_valiator()
        user = self.model.create_user(**data)
        serializer = self.get_serializer(
            user,
            context
        )
        return Response(
            {
                "message": "Registration successful",
                "data": serializer.data
            },
            status.HTTP_201_CREATED
        )

    @action(methods=["POST"], permission_classes=[])
    def login(self, request):
        data,context = self.request_valiator()
        user = authenticate(**data)
        serializer = self.get_serializer(
            user,
            context
        )
        return Response(
            {
                "message": "Login successful",
                "data": serializer.data
            }
        )
        

    @action(methods=["POST"], permission_classes=[])
    def logout(self, request):
        request.auth.delete()
        return Response(
            {
                "message": "Logout Succcessful"
            }
        )
        


