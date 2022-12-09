from django.urls import path
from .views import (
    EventView,
    # HomeIndex,
    # index
)

urlpatterns = [
    path("events", EventView.as_view()),
    # path("contact-us", ContactUsView.as_view()),
    # path("contact-us/<str:pk>", ContactUsView.as_view()),
]