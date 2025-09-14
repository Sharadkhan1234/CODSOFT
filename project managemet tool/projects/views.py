from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.db.models import Q, Count
from .models import Project, Task, ProjectMembership
from .forms import ProjectForm, TaskForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Project

class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description', 'deadline']
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')  # 👈 redirect to list after creating


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/project_list.html'
    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(Q(owner=user) | Q(collaborators=user)).distinct()
class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project; form_class = ProjectForm; template_name = 'projects/project_form.html'
    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        ProjectMembership.objects.create(user=self.request.user, project=self.object, role='manager')
        return response
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task; form_class = TaskForm; template_name = 'projects/task_form.html'
    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=kwargs.get(
            'project_pk'))
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        form.instance.project = self.project
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.project.pk})
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task; form_class = TaskForm; template_name = 'projects/task_form.html'
    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.project.pk})
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'projects/dashboard.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.user
        projects = Project.objects.filter(Q(owner=user) | Q(collaborators=user)).distinct()
        tasks = Task.objects.filter(project__in=projects)
        ctx['projects_count'] = projects.count()
        ctx['tasks_by_status'] = list(tasks.values('status').annotate(count=Count('id')))
        ctx['overdue_count'] = tasks.filter(due_date__lt=timezone.localdate()).count()
        ctx['tasks'] = tasks.order_by('due_date')[:20]
        return ctx
class KanbanView(LoginRequiredMixin, TemplateView):
    template_name = 'projects/kanban.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        project = get_object_or_404(Project, pk=kwargs.get('pk'))
        ctx['project'] = project
        ctx['todo'] = project.tasks.filter(status='todo')
        ctx['in_progress'] = project.tasks.filter(status='in_progress')
        ctx['done'] = project.tasks.filter(status='done')
        return ctx
