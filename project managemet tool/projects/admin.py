from django.contrib import admin
from .models import Project, ProjectMembership, Task, Comment
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=('name','owner','created_at')
    search_fields=('name','description')
@admin.register(ProjectMembership)
class ProjectMembershipAdmin(admin.ModelAdmin):
    list_display=('project','user','role')
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=('title','project','assignee','status','priority','due_date','progress')
    list_filter=('status','priority')
    search_fields=('title','description')
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('task','author','created_at')
