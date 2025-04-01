from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # Здесь для простоты связываем видео с пользователем, который его загрузил
    user = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title