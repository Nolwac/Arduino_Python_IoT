from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('switch/<id>/', switch_device, name='switch'),
    path('receive_state/<id>/', show_state, name='show_state')
]
