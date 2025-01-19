from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
path('careers/', views.root),
path('careers/<int:id>', views.itemMutate),
]
