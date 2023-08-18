from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from .views import PostViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls

static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)