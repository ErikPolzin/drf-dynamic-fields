from django.contrib.auth.models import User

from dynamic_fields.serializers import DynamicFieldsModelSerializer


class UserSerializer(DynamicFieldsModelSerializer):
    """Serializes User objects to JSON."""

    class Meta:
        model = User
        fields = "__all__"
