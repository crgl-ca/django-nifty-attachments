from __future__ import annotations

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AttachmentsConfig(AppConfig):
    name = "nifty_attachments"
    verbose_name = _("Nifty Attachments")
