from django.urls import path

from .views import UserListView, UserUpToAdminView,UserUpdeteProfileView

urlpatterns = [
    path('', UserListView.as_view(), name='all_users'),
    path('/<int:pk>/to_admin', UserUpToAdminView.as_view(), name='up_to_admin'),
    path('/<int:pk>/profile', UserUpdeteProfileView.as_view(), name='update_profile')
]
