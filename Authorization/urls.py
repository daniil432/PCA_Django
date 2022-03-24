from django.urls import path
from . import views

urlpatterns = [
    path('', views.authorization),
    path('AboutUs', views.AboutView),
    path('Homepage', views.HomepageView),
    path('Members', views.MembersView)
]
