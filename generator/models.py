from django.db import models
NULLABLE = {'blank': True, 'null': True}

class Video(models.Model):

    video_file = models.FileField(upload_to='video/')

    title = models.CharField(max_length=100, **NULLABLE, verbose_name='Название')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')

    def __str__(self):
        return self.title or 'Видео'

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'