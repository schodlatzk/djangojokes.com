from django.contrib import admin
from django.urls import path, include

app_name = 'jokes'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('jokes/', include('jokes.urls')),
    path('', include('pages.urls')),
]