from menu.apps import MenuConfig
from django.urls import path
from menu.views import MenuDetailView


app_name = MenuConfig.name


urlpatterns = [
    path('menu/<int:pk>/', MenuDetailView.as_view(), name='menu'),
]
