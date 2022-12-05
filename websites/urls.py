from django.urls import path
from .views import (
    ContactUsView,
    HomeIndex
)

urlpatterns = [
    path("", HomeIndex.as_view()),
    path("contact-us", ContactUsView.as_view()),
    path("contact-us/<str:pk>", ContactUsView.as_view()),
]
