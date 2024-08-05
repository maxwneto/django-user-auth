# mf_project/urls.py
from django.contrib import admin
from django.urls import include, path
from users import views  # Adjust according to your main app structure

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', views.home, name='home'),
    #path('', include('django.contrib.auth.urls')),  # For built-in authentication views
]
