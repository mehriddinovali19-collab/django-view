from django.urls import path 
from . views import ItemView, item_view

urlpatterns = [
    path('items-fbv/', ItemView.as_view(), name='item-url'),
    path('items-cbv/', item_view.as_view(), name='item-url')
]