from django.urls import path
from .views import Menus, MenuDetailView, MenuItemChildDetailView

urlpatterns = [
    path('', Menus.as_view(), name='menus'),
    path('<slug:slug>/', MenuDetailView.as_view(), name='menu_detail_view'),
    path('child/<slug:slug>/', MenuItemChildDetailView.as_view(), name='child_detail_view'),
]