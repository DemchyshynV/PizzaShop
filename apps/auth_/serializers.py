from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

from apps.user_profile.serializers import ProfileCreateSerializer

UserModel = get_user_model()


class RegisterSerializer(ModelSerializer):
    profile = ProfileCreateSerializer()

    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password', 'profile')

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        serializer = ProfileCreateSerializer(data=profile)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return user

