from django import forms
from .models import Project, Task, Comment
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','description','collaborators']
class TaskForm(forms.ModelForm):
    due_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Task
        fields = ['title','description','assignee','status','priority','due_date','progress','attachment']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'collaborators']
