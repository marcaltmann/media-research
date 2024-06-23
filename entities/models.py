from django.db import models
from django.utils.translation import gettext_lazy as _


class Entity(models.Model):
    TYPE_PERSON = "PER"
    TYPE_LOCATION = "LOC"
    TYPE_ORGANISATION = "ORG"
    TYPE_MISC = "MISC"
    TYPE_CHOICES = (
        (TYPE_PERSON, _("Person")),
        (TYPE_LOCATION, _("Location")),
        (TYPE_ORGANISATION, _("Organisation")),
        (TYPE_MISC, _("Misc")),
    )
    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
    )
    name = models.CharField(_("name"), max_length=255)
    gnd_id = models.CharField(_("GND id"), max_length=20, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = _("entity")
        verbose_name_plural = _("entities")

    def __str__(self):
        return self.name


class Location(Entity):
    geonames_id = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Organisation(Entity):
    pass


class Misc(Entity):
    pass


class Person(models.Model):
    MALE = "M"
    FEMALE = "F"
    DIVERSE = "D"
    UNSPECIFIED = "N"
    GENDER_CHOICES = {
        MALE: "Male",
        FEMALE: "Female",
        DIVERSE: "Diverse",
        UNSPECIFIED: "Not specified",
    }

    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200)
    eastern_name_order = models.BooleanField(
        _("eastern name order"),
        default=False,
        help_text=_("Select if the last name should appear first."),
    )
    gnd_id = models.CharField(
        _("GND id"),
        max_length=20,
        blank=True,
        help_text="<a href='https://d-nb.info/standards/elementset/gnd'>GND</a> authority file identifier",
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=UNSPECIFIED,
    )
    date_of_birth = models.DateField()

    def fullname(self):
        if self.eastern_name_order:
            return f"{self.last_name} {self.first_name}"
        else:
            return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullname()

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = _("person")
        verbose_name_plural = _("people")
