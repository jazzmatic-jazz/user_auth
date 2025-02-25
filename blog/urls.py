from django.urls import path
from .views import get_blogs, create_blog, doc_blogs


urlpatterns = [
    path("", get_blogs, name="blogs"),
    path("create/", create_blog, name="create_blog"),
    path("doc_blog/", doc_blogs, name="doc_blog"),
]
