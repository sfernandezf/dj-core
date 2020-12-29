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
        default_permissions = ("view", "add", "change", "delete")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_timestamp = models.DateTimeField(
        _("Created At"), auto_now_add=True, editable=False
    )
    updated_timestamp = models.DateTimeField(
        _("Updated At"), auto_now=True, editable=False
    )


class ViewerUserMixinModel(models.Model):
    """
    Abstract ViewerUser Mixib Model
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._viewer_user = None

    class Meta:
        abstract = True

    @property
    def viewer_user(self):
        return self._viewer_user

    def set_viewer_user(self, user):
        self._viewer_user = user
