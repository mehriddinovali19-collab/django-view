from django.urls import path 
from . views import ItemView, item_view

urlpatterns = [
    path('items-cbv/', ItemView.as_view(), name='item-url'),
    path('items-fbv/', item_view, name='item-url')
]