from django.test import TestCase
from django.urls import reverse

from archive.models import Collection

def create_collection(name):
    """
    Create a collection with the given `name`.
    """
    return Collection.objects.create(name=name)


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
