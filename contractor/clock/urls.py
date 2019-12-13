from django.urls import path

from clock.views import ClockList
from clock import views


urlpatterns = [
    path("", ClockList.as_view(), name="clock-list"),
    path("down/", views.tickdown, name="tick-down"),
    path("up/", views.tickup, name="tick-up"),
    path("rem/", views.delete, name="tick-delete")
]
