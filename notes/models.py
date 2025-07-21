from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_important = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50)
    notes = models.ManyToManyField(Note, related_name='tags')

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Reminder(models.Model):
    note = models.OneToOneField(Note, on_delete=models.CASCADE)
    remind_at = models.DateTimeField()

    def __str__(self):
        return f"Reminder for: {self.note.title} at {self.remind_at}"
