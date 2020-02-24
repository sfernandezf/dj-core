import uuid as uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    """
    Abstract Base Model
    """

    class Meta:
        abstract = True
        ordering = ("-created_timestamp",)
        default_permissions = ('view', 'add', 'change', 'delete')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_timestamp = models.DateTimeField(_("Created At"), auto_now_add=True, 
                                             editable=False)
    updated_timestamp = models.DateTimeField(_("Updated At"), auto_now=True, 
                                             editable=False)
