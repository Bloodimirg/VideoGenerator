import os
import tempfile
import urllib

from django.core.files import File
from django.http import HttpResponse
from django.views.generic import TemplateView
from moviepy.editor import TextClip, ColorClip, CompositeVideoClip
from rest_framework.viewsets import ViewSet

from generator.models import Video


class HomePageView(TemplateView):
    """Главная страница"""
    template_name = 'generator/base.html'


class VideoViewSet(ViewSet):
    """Генерация видео"""
    def video_generator(self, request):
        # Параметры видео
        video_duration = 3
        video_size = (100, 100)
        text = request.GET.get('text', 'Hello!')
        file_name = text

        # Создание текстового клипа (бегущей строки)
        text_clip = TextClip(
            text,
            fontsize=50,
            color='white',
            font='Arial'
        ).set_duration(video_duration)

        # Перемещение текста по горизонтали (эффект "бегущей строки")
        text_clip = text_clip.set_position(lambda t: (100 - 100 * t, 'bottom'))

        # Создание фонового клипа с фиолетовым фоном
        background_clip = ColorClip(size=video_size, color=(255, 0, 255)).set_duration(video_duration)

        video = CompositeVideoClip([background_clip, text_clip])

        # Декодируем для правильного названия файла
        encoded_file_name = urllib.parse.quote(f"{file_name}.mp4")

        # Генерация временного файла для сохранения видео
        with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp_file:
            video.write_videofile(temp_file.name, fps=24)

            with open(temp_file.name, 'rb') as f:
                django_file = File(f)
                video_instance = Video(title=text)
                video_instance.video_file.save(f"{file_name}.mp4", django_file, save=True)

            # Чтение сгенерированного файла и отправка его как ответ
            with open(temp_file.name, 'rb') as f:
                response = HttpResponse(f.read(), content_type='video/mp4')
                response['Content-Disposition'] = f"attachment; filename*=UTF-8''{encoded_file_name}"

            os.remove(temp_file.name)
        return response
