from django.db import models
from django.template.defaultfilters import escape
from hueb.apps.hueb20.models.utils import HUEB20, HUEB_APPLICATIONS
from simple_history.models import HistoricalRecords

from .culturalCircle import CulturalCircle
from .document import Document
from .person import Person


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    external = models.BooleanField(
        default=False,
        help_text="External comments will be displayed on the public website.",
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="person_comment",
    )
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="document_comment",
    )
    cultural_circle = models.ForeignKey(
        CulturalCircle,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="cultural_circle_comment",
    )
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    history = HistoricalRecords()

    def __str__(self):
        if self.text is None:
            return " "
        return escape(self.text)
