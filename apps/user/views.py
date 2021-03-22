from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView, UpdateAPIView, get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.response import Response

from apps.user_profile.serializers import ProfileDetailSerializer
from .serializers import UserDetailSerialiser
from .permissions import IsSuperUser

UserModel = get_user_model()


class UserListView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = UserModel.objects.all()
    serializer_class = UserDetailSerialiser


class UserUpToAdminView(GenericAPIView):
    queryset = UserModel.objects
    permission_classes = [IsSuperUser]

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serialiser = UserDetailSerialiser(user)
        return Response(serialiser.data, status.HTTP_200_OK)


class UserUpdeteProfileView(UpdateAPIView):
    serializer_class = ProfileDetailSerializer

    def get_permissions(self):
        pk = self.kwargs.get('pk')
        if self.request.user.id != pk:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_object(self):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        return user.profile
