from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from dynamic_fields.mixins import DynamicFieldsViewMixin
from .serializers import UserSerializer


class UserViewSet(DynamicFieldsViewMixin, ModelViewSet):
    """View/Edit/Add/Delete User objects."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
