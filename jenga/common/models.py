import uuid

from django.db import models
from django.utils import timezone


class AbstractBase(models.Model):
    """
    Base class to be inherited by `jenga` models.
    """
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created = models.DateTimeField(db_index=True, default=timezone.now)
    updated = models.DateTimeField(db_index=True, default=timezone.now)

    class Meta:
        abstract = True
        ordering = ('-updated', '-created',)
