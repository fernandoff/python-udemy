from django.urls import path
from .views import review, feedback

urlpatterns = [
    path("", review),
    path("feedback", feedback, name="feedback")
]
