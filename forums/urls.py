from django.urls import path
from . import views

app_name = 'forums'

urlpatterns = [
    path('', views.index, name="index"),
    path('<forum_id>', views.show, name="show"),
    path('forum_json/', views.ForumJsonView.as_view()),
    path('test_methods/', views.test_methods, name="test_methods"),
    path('test_methods2/', views.TestMethodsView.as_view(), name="test_methods2"),
    path('topics/', views.TopicListView.as_view(), name="topics"),
    path('topics/<int:pk>', views.TopicDetailView.as_view(), name='topic_details'),
    path('topics/create', views.TopicCreateView.as_view(), name='topic_create'),
    path('topics/<int:pk>/update', views.TopicUpdateView.as_view(), name='topic_update'),
    path('file_upload/', views.FileUploadView.as_view())
]
