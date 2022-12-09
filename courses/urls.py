from django.urls import path
from .views import (
    CourseView,
    # HomeIndex,
    # index
)

urlpatterns = [
    path("course", CourseView.as_view()),
    # path("contact-us", ContactUsView.as_view()),
    # path("contact-us/<str:pk>", ContactUsView.as_view()),
]
