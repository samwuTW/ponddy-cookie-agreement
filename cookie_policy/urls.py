from django.urls import path
from . import views


urlpatterns = [
    path('accept', views.accept, name='cookie_policy_accept'),
]
