from django.urls import path
from websites.views import (
    # ContactUsView,
    # HomeIndex,
    index
)

urlpatterns = [
    path("", index, name="index"),
    # path("contact-us", ContactUsView.as_view()),
    # path("contact-us/<str:pk>", ContactUsView.as_view()),
]
