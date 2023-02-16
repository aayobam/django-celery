from django.urls import path
from .import views




urlpatterns = [
    path("", views.ContactUsView.as_view(), name="contact-us"),
    path("success/", views.SuccessView.as_view(), name="success"),
]
