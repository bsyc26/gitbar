from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='codes'),
    path('<int:code_id>', views.code, name='code'),
    path('search', views.search, name='search'),
]
