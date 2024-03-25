from django.test import TestCase

from .models import Interview


class InterviewModelTests(TestCase):
    def test_is_video_with_video(self):
        """ is_video() returns True for videos. """
        video = Interview(media_type="video/mp4")
        self.assertIs(video.is_video(), True)

    def test_is_video_with_other(self):
        """ is_video() returns False for non-videos. """
        audio = Interview(media_type="audio/mp3")
        self.assertIs(audio.is_video(), False)

    def test_is_audio_with_audio(self):
        """ is_audio() returns True for audios. """
        audio = Interview(media_type="audio/mp3")
        self.assertIs(audio.is_audio(), True)

    def test_is_audio_with_other(self):
        """ is_audio() returns False for non-audios. """
        video = Interview(media_type="video/mp4")
        self.assertIs(video.is_audio(), False)
