from rest_framework.routers import DefaultRouter
from .api_views import ProjectViewSet, TaskViewSet, CommentViewSet
router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('tasks', TaskViewSet)
router.register('comments', CommentViewSet)
urlpatterns = router.urls
