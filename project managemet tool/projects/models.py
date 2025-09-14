from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, related_name='owned_projects', on_delete=models.CASCADE)
    collaborators = models.ManyToManyField(User, related_name='collaborations', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return self.name
class ProjectMembership(models.Model):
    ROLE_CHOICES = [('manager','Manager'),('developer','Developer'),('viewer','Viewer')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='memberships')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='developer')
    class Meta:
        unique_together = ('user','project')
    def __str__(self): return f"{self.user} — {self.project} ({self.role})"
class Task(models.Model):
    STATUS_CHOICES = [('todo','To Do'),('in_progress','In Progress'),('done','Done')]
    PRIORITY_CHOICES = [(1,'Low'),(2,'Medium'),(3,'High')]
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    assignee = models.ForeignKey(User, related_name='tasks', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    due_date = models.DateField(null=True, blank=True)
    progress = models.IntegerField(default=0)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return f"{self.title} — {self.project.name}"
    @property
    def overdue(self):
        from django.utils import timezone
        if self.due_date:
            return self.due_date < timezone.localdate()
        return False
class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Comment by {self.author} on {self.task.title}"
from django.urls import reverse
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("project_list")   # 👈 redirects after save
def get_absolute_url(self):
    return reverse("project_detail", kwargs={"pk": self.pk})

from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField(null=True, blank=True)

    # Add collaborators
    collaborators = models.ManyToManyField(User, related_name="projects", blank=True)

    def __str__(self):
        return self.name

