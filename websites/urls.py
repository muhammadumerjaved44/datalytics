from django.urls import path
from .views import (
    ContactView,
    HomeIndex
)

urlpatterns = [
    path("", HomeIndex.as_view()),
    path("contact-us", ContactView.as_view()),
    path("contact-us/<str:pk>", ContactView.as_view()),
]
