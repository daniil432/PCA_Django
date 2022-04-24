from django.urls import path
from . import views


urlpatterns = [
    path('', views.Graph, name='Graph'),
    path('<int:param>', views.testview, name='testview'),
]
