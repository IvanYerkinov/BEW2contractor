from django.urls import path

from .views import ClockList, ClockDetail

urlpatterns = [
    path("clocks/", ClockList.as_view(), name="clock_list"),
    path('clocks/<int:id>/', ClockDetail.as_view(), name="clock_detail")

]
