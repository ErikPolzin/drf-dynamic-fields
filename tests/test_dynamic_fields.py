from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory

from .serializers import UserSerializer
from .views import UserViewSet



class DynamicFieldsTestCase(TestCase):

    def setUp(self):
        User.objects.create(username="johndoe", first_name="John", last_name="Doe", email="john@example.com")
        User.objects.create(username="janedoe", first_name="Jane", last_name="Doe", email="jane@example.com")
        self.factory = APIRequestFactory()

    def test_dynamic_fields_mixin_returns_field_subset(self):
        view = UserViewSet.as_view({'get': 'list'})
        request = self.factory.get('/users/?fields=first_name&fields=last_name')
        response = view(request)
        assert response.data[0].keys() == {"first_name", "last_name"}

    def test_no_dynamic_fields_returns_all_fields(self):
        view = UserViewSet.as_view({'get': 'list'})
        request = self.factory.get('/users/')
        response = view(request)
        assert response.data[0].keys() == UserSerializer().get_fields().keys()