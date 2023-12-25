from django.urls import path
from .views import homeview, ServiceView, AboutView, TeamView, WhyView

app_name = 'core'
urlpatterns = [
    path('', homeview, name="home_page"),
    path('service/', ServiceView.as_view(), name="service_page"),
    path('about/', AboutView.as_view(), name="about_page"),
    path('team/', TeamView.as_view(), name="team_page"),
    path('why/', WhyView.as_view(), name="why_page"),
]