from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from makerschatbot.clases.abstract.audit_mixin import AuditMixin
from makerschatbot.variables.schemas import Schema
from .chat import Chat

class Prompt(AuditMixin):
    """
    Chat Prompt.

    Represents a specific user prompt and its corresponding response
    within a chat conversation, storing both the input and AI response.
    """

    id = models.UUIDField(
        primary_key=True,
        verbose_name=_("Prompt ID"),
        db_comment=_("Unique identifier for the chat prompt")
    )
    
    chat = models.ForeignKey(
        Chat,
        on_delete=models.PROTECT,
        related_name='prompts',
        verbose_name=_("Associated Chat"),
        db_comment=_("Chat conversation containing this prompt")
    )

    prompt = models.TextField(
        verbose_name=_("User Prompt"),
        db_comment=_("Full text of the user's input prompt")
    )

    class Meta:
        verbose_name = _("Chat Prompt")
        verbose_name_plural = _("Chat Prompts")
        db_table = f'"{Schema.chat}"."prompt"'
        db_table_comment = _("Stores all prompts and responses within chat conversations")