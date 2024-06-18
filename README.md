# Dynamic Fields for Django Rest Framework

Allows specifying a subset of fields in the rest framework URL.

## Quickstart

Say I've exposed a URL `/api/users/` that serializes a list of users (using django's built-in user model).
By default, the serializer will include or exclude the fields that you specify in its Meta's `fields` attribute.
If we want to allow returning a subset of fields based on the GET parameters, we must change the following:

1. Make sure the serializer inherits from `dynamic_fields.serializers.DynamicFieldsModelSerializer`
2. Use the `dynamic_fields.mixins.DynamicFieldsViewMixin` in our view

The code might look something like this:
```python
# serializers.py
from django.contrib.auth.models import User
from dynamic_fields.serializers import DynamicFieldsModelSerializer


class UserSerializer(DynamicFieldsModelSerializer):
    """Serializes User objects to JSON."""

    class Meta:
        model = User
        fields = "__all__"
```

```python
# views.py
from django.contrib.auth.models import User
from dynamic_fields.mixins import DynamicFieldsViewMixin
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer


class UserViewSet(DynamicFieldsViewMixin, ModelViewSet):
    """View/Edit/Add/Delete User objects."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
```

Now when the client calls a URL like `/api/users/?fields=username&fields=first_name` the API will only return the `username` and `first_name` fields.