from django.contrib import admin
from django.urls import path

from . import views

app_name = 'forums'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('<forum_id>', views.show, name="show"),
]
