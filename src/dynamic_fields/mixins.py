from .serializers import DynamicFieldsModelSerializer


class DynamicFieldsViewMixin:
    """Allows modifying the serializer to only include a subset of fields.
    
    The API can be called with e.g. /api/users/?fields=username&fields=first_name
    which will only include the 'username' and 'first_name' fields.
    """

    def get_serializer(self, *args, **kwargs):
        """Set the serializer 'fields' parameter."""
        assert issubclass(self.serializer_class, DynamicFieldsModelSerializer), \
            "Serializer must be a DynamicFieldsModelSerializer type"
        if self.request.method == "GET":
            kwargs["fields"] = self.request.GET.getlist("fields") or None
        return super().get_serializer(*args, **kwargs)
