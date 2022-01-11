from collections import UserList
from django.urls import path
from .views import ListDetail, ListView, UserDetail, index, UserList
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', index, name='index'),
    path('list/', ListView.as_view(), name="list_view"),
    path('list/<int:pk>', ListDetail.as_view(), name="list_detail"),
    path('users/', UserList.as_view(), name="users_list"),
    path('users/<int:pk>', UserDetail.as_view(), name="users_detail"),
]



# URLS DE AUTENTICAÇÃO
urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]