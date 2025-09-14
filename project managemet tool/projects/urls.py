from django.urls import path
from .views import ProjectListView, ProjectDetailView, ProjectCreateView, TaskCreateView, TaskUpdateView, DashboardView, KanbanView
urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:project_pk>/tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('projects/<int:pk>/kanban/', KanbanView.as_view(), name='kanban'),
]
