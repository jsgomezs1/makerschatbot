import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from makerschatbot.clases.abstract.audit_mixin import AuditMixin
from makerschatbot.variables.schemas import Schema
from .prompt import Prompt

class Response(models.Model):
    """
    Chat Response.

    Stores the chatbot's response to a user prompt along with optional
    user feedback and rating for quality assessment.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("Response ID"),
        db_comment=_("Unique identifier for the chat response")
    )
    
    prompt = models.ForeignKey(
        Prompt,
        on_delete=models.PROTECT,
        related_name='responses',
        verbose_name=_("Related Prompt"),
        db_comment=_("Original user prompt that generated this response")
    )

    content = models.TextField(
        verbose_name=_("Chatbot Response"),
        db_comment=_("Full text of the AI-generated response to the user")
    )

    rating = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(0.00, _('Minimum rating is 0.00 (Very poor)')),
            MaxValueValidator(100.00, _('Maximum rating is 100.00 (Excellent)'))
        ],
        verbose_name=_("User Rating"),
        db_comment=_("User-provided quality rating for the chatbot response. "
                    "Decimal value between 0.00 (Very poor) and 100.00 (Excellent)."),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _("Chat Response")
        verbose_name_plural = _("Chat Responses")
        db_table = f'"{Schema.chat}"."response"'
        db_table_comment = _("Stores chatbot responses and user ratings for quality analysis")