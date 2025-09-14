from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Task
@receiver(pre_save, sender=Task)
def notify_on_assign(sender, instance, **kwargs):
    try:
        old = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        old = None
    if old is None and instance.assignee:
        subject = f'You have been assigned task: {instance.title}'
        message = f'Hello,\n\nYou were assigned the task "{instance.title}" in project {instance.project}.\n'
        if instance.assignee.email:
            send_mail(subject, message, 'no-reply@example.com', [instance.assignee.email], fail_silently=True)
    elif old and old.assignee != instance.assignee and instance.assignee:
        subject = f'You have been assigned task: {instance.title}'
        message = f'Hello,\n\nAssignment changed; you are now assigned the task "{instance.title}" in project {instance.project}.\n'
        if instance.assignee.email:
            send_mail(subject, message, 'no-reply@example.com', [instance.assignee.email], fail_silently=True)
