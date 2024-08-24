from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class CustomUser(AbstractUser):
    public_visibility = models.BooleanField(default=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    birth_year = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.age and self.birth_year:
            from datetime import datetime
            current_year = datetime.now().year
            self.age = current_year - self.birth_year
        super().save(*args, **kwargs)



class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='uploaded_files/')
    visibility = models.CharField(max_length=7, choices=[('public', 'Public'), ('private', 'Private')])
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    year_of_published = models.PositiveIntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title