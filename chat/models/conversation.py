from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from makerschatbot.clases.abstract.audit_mixin import AuditMixin
from makerschatbot.variables.schemas import Schema

class Conversation(AuditMixin):
    """
    Conversación.

    Representa una conversación en el sistema, la cual actúa como cabecera o contenedor
    para múltiples interacciones (detalles de conversación) relacionadas con un chat específico.
    """

    id = models.UUIDField(
        primary_key=True,
        verbose_name=_("ID de Conversación"),
        db_comment=_("Identificador único para la conversación.")
    )
    
    name = models.CharField(
        max_length=255,
        verbose_name=_("Nombre de la Conversación"),
        db_comment=_("Nombre o título descriptivo de la conversación.")
    )

    class Meta:
        verbose_name = _("Conversación")
        verbose_name_plural = _("Conversaciones")
        db_table = f'"{Schema.chat}"."conversation"'
        db_table_comment = _("Conversación: almacena el título o cabecera de cada chat, el cual tiene relacionados múltiples detalles de conversación (ConversationDetail).")