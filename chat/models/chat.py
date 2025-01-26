import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from makerschatbot.clases.abstract.audit_mixin import AuditMixin
from makerschatbot.variables.schemas import Schema

class Chat(AuditMixin):
    """
    Chat.

    Representa un chat en el sistema, el cual actúa como cabecera o contenedor
    para múltiples interacciones (detalles de chat) relacionadas con una conversación específica.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("ID del Chat"),
        db_comment=_("Identificador único para el chat.")
    )
    
    name = models.CharField(
        max_length=255,
        verbose_name=_("Nombre del Chat"),
        db_comment=_("Nombre o título descriptivo del chat.")
    )

    class Meta:
        verbose_name = _("Chat")
        verbose_name_plural = _("Chats")
        db_table = f'"{Schema.chat}"."chat"'
        db_table_comment = _("Chat: almacena el título o cabecera de cada chat, el cual tiene relacionados múltiples detalles de interacción (ChatDetail).")