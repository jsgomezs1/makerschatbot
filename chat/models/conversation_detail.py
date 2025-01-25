from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from makerschatbot.clases.abstract.audit_mixin import AuditMixin
from makerschatbot.variables.schemas import Schema
from .conversation import Conversation

class ConversationDetail(AuditMixin):
    """
    Detalle de Conversación.

    Un detalle de conversación representa una interacción específica de pregunta-respuesta
    dentro de una conversación.
    """

    id = models.UUIDField(
        primary_key=True,
        verbose_name=_("ID del Detalle de Conversación"),
        db_comment=_("Identificador único para el detalle de conversación.")
    )
    
    Conversation = models.ForeignKey(
        Conversation,
        on_delete=models.PROTECT,
        related_name='Conversation_details',
        verbose_name=_("Cabecera de Conversación"),
        db_comment=_("Cabecera de conversación asociada a este detalle.")
    )

    question = models.TextField(
        verbose_name=_("Pregunta"),
        db_comment=_("Texto de la pregunta realizada.")
    )

    answer = models.TextField(
        verbose_name=_("Respuesta"),
        db_comment=_("Texto de la respuesta proporcionada.")
    )

    rating = models.DecimalField(
        max_digits=5,  # Número total de dígitos, incluyendo los decimales
        decimal_places=2,  # Número de dígitos decimales
        validators=[
            MinValueValidator(0.00, _('La calificación mínima es 0.00 (Muy mal)')),
            MaxValueValidator(100.00, _('La calificación máxima es 100.00 (Excelente)'))
        ],
        verbose_name=_("Calificación del Chatbot"),
        db_comment=_("Calificación proporcionada por el usuario para la respuesta del chatbot. "
                    "Debe ser un valor decimal entre 0.00 (Muy mal) y 100.00 (Excelente).")
    )

    class Meta:
        verbose_name = _("Detalle de Conversación")
        verbose_name_plural = _("Detalles de Conversación")
        db_table = f'"{Schema.chat}"."conversation_detail"'
        db_table_comment = _("Detalle del chat: registra el detalle de la conversación de cada chat")