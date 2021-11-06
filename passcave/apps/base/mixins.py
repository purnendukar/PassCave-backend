class MultiSerializerMixin:
    serializer_classes = {}

    def get_serializer_class(self):
        if self.action in self.serializer_classes:
            return self.serializer_classes[self.action]
        return super().get_serializer_class()


class MultiRequestValidatorMixin:
    request_serializer_classes = {}

    def request_valiator(self):
        if self.action in self.request_serializer_classes:
            serializer = self.request_serializer_classes[self.action](
                data=self.request.data
            )
        else:
            serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        return (serializer.validated_data, serializer.context)


class MultiSerializerMixin:
    serializer_classes = {}

    def get_serializer_class(self):
        if self.action in self.serializer_classes:
            serializer = self.serializer_classes[self.action]
        else:
            serializer = super().get_serializer_class()
        return serializer
