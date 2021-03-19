from django.urls import path, include

urlpatterns = [
    path('/auth', include('apps.auth_.urls')),
    path('/users', include('apps.user.urls')),
    path('/profiles', include('apps.user_profile.urls'))
]
