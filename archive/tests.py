from django.test import TestCase
from django.urls import reverse

from .models import Interview, Collection

def video():
    return Interview(media_type="video/mp4")


def audio():
    return Interview(media_type="audio/mp3")


def create_collection(name):
    """
    Create a collection with the given `name`.
    """
    return Collection.objects.create(name=name)


class InterviewModelTests(TestCase):
    def test_is_video_with_video(self):
        """ is_video() returns True for videos. """
        self.assertIs(video().is_video(), True)

    def test_is_video_with_other(self):
        """ is_video() returns False for non-videos. """
        self.assertIs(audio().is_video(), False)

    def test_is_audio_with_audio(self):
        """ is_audio() returns True for audios. """
        self.assertIs(audio().is_audio(), True)

    def test_is_audio_with_other(self):
        """ is_audio() returns False for non-audios. """
        self.assertIs(video().is_audio(), False)


class CollectionIndexViewTests(TestCase):
    def test_no_collections(self):
        """
        If no collections exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("archive:collection_index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No collections are available.")
        self.assertQuerySetEqual(response.context["collection_list"], [])

    def test_single_collection(self):
        """
        Single collection is displayed on the index page.
        """
        collection = create_collection(name="First collection")
        response = self.client.get(reverse("archive:collection_index"))
        self.assertQuerySetEqual(
            response.context["collection_list"],
            [collection],
        )

    def test_multiple_collections(self):
        """
        Two collections are displayed in the correct order.
        """
        collection1 = create_collection(name="Beta")
        collection2 = create_collection(name="Alpha")
        response = self.client.get(reverse("archive:collection_index"))
        self.assertQuerySetEqual(
            response.context["collection_list"],
            [collection2, collection1],
        )
