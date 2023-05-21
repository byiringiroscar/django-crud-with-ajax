# urls.py

from django.urls import path
from crud_ajax import  views

urlpatterns = [
    path('crud/',  views.CrudView.as_view(), name='crud_ajax'),
]