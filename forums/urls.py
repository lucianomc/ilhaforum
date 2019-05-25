from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<forum_id>', views.show, name="show"),
    path('topics/', views.TopicListView.as_view(), name="topics")
]
