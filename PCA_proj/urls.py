from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Authorization.urls')),
    path('InputPage', include('PCA_app.urls')),
    path('register', include('Registration.urls')),
]
