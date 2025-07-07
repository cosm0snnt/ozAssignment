from django.urls import path
from . import views

urlpatterns = \
[
    path("", views.Feeds.as_view()), # 127.0.0.1:8000/api/v1/feeds
    path("<int:feed_id>", views.FeedDetail.as_view()),
]