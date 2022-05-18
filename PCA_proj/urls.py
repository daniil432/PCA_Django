from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Authorization.urls')),
    path('admin', admin.site.urls),
    path('InputPage', include('PCA_app.urls')),
    path('Register', include('Registration.urls')),
    path('Graph_App/', include('Graph_App.urls')),

]
