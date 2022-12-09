from django.urls import path
from .views import (
    ClientsView,
    # HomeIndex,
    # index
)

urlpatterns = [
    path("clients", ClientsView.as_view()),
    # path("contact-us", ContactUsView.as_view()),
    # path("contact-us/<str:pk>", ContactUsView.as_view()),
]