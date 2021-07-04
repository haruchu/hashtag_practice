from django.urls import path
from .views import FormClass, ListClass

urlpatterns = [
    path('', ListClass.as_view(), name='list'),
    path('form/', FormClass.as_view(), name='form'),
]
