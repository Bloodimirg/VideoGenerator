import os
import tempfile

from django.http import HttpResponse
from moviepy.editor import TextClip, ColorClip, CompositeVideoClip
from rest_framework.viewsets import ViewSet


class VideoViewSet(ViewSet):

    def video_generator(self, request):
        # Параметры видео
        video_duration = 3
        video_size = (100, 100)
        text = "Салют"

        # Создание текстового клипа (бегущей строки)
        text_clip = TextClip(
            text,
            fontsize=70,
            color='white',
            font='Arial'
        ).set_duration(video_duration)

        # Перемещение текста по горизонтали (эффект "бегущей строки")
        text_clip = text_clip.set_position(lambda t: (100 - 100*t, 'bottom'))

        # Создание фонового клипа с фиолетовым фоном
        background_clip = ColorClip(size=video_size, color=(255, 0, 255)).set_duration(video_duration)


        video = CompositeVideoClip([background_clip, text_clip])

        # Генерация временного файла для сохранения видео
        with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp_file:
            video.write_videofile(temp_file.name, fps=24)

            # Чтение сгенерированного файла и отправка его как ответ
            with open(temp_file.name, 'rb') as f:
                response = HttpResponse(f.read(), content_type='video/mp4')
                response['Content-Disposition'] = 'attachment; filename="video.mp4"'

            # Удаление временного файла
            os.remove(temp_file.name)

        return response
