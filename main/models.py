from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UploadDataset(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    file_in_memory = models.FileField(upload_to='uploads/')
    share = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file_in_memory.name