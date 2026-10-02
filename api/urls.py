from django.urls import path 
from . views import ItemView, item_view, UserCreateView

urlpatterns = [
    path('items-cbv/', ItemView.as_view(), name='item-cbv-url'),
    path('items-fbv/', item_view, name='item-fbv-url'),
    path('users/', UserCreateView.as_view(), name='user-url'),
]