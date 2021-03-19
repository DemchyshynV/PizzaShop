from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model

from .serializers import UserDetailSerialiser

UserModel = get_user_model()


class UserListView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserDetailSerialiser
