class MultiSerializerViewMixin:
    serializer_classes = {}

    def get_serializer_class(self):
        if self.actions in self.serializer_classes:
            return self.serializer_classes[self.actions]
        return super().get_serializer_class()


class MultiRequestValidatorViewMixin:
    request_serializer_classes = {}

    def request_valiator(self):
        serializer = self.request_serializer_classes[self.actions](self.request.data)
        return (serializer.validated_data, serializer.context)
