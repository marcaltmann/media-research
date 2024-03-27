from django.test import TestCase
from django.urls import reverse

from archive.models import Collection, Location

def create_collection(name):
    """
    Create a collection with the given `name`.
    """
    return Collection.objects.create(name=name)


def create_location(name, lat, lng):
    """
    Create a location with the given `name`.
    """
    return Location.objects.create(name=name, latitude=lat, longitude=lng)


class CollectionIndexViewTests(TestCase):
    def test_no_collections(self):
        """
        If no collections exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("archive:collection_index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No collections are available.")
        self.assertQuerySetEqual(response.context["collection_list"], [])

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


class MapViewTests(TestCase):
    def test_no_locations(self):
        """
        If no locations exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("archive:map"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No locations are available.")
        self.assertQuerySetEqual(response.context["location_list"], [])

    def test_multiple_locations(self):
        """
        Two locations are put in the context.
        """
        location1 = create_location("Paris", 50, 10)
        location2 = create_location("Berlin", 30, 10)
        response = self.client.get(reverse("archive:map"))
        self.assertQuerySetEqual(
            response.context["location_list"],
            [location1, location2],
            ordered=False,
        )
