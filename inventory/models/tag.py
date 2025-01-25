from django.forms import ValidationError
from makerschatbot.clases.abstract.audit_mixin import AuditMixin
from makerschatbot.variables.schemas import Schema
from django.utils.translation import gettext_lazy as _ 
from django.db import models
import uuid

class Tag(models.Model):
    """
    Tag.

    Una Etiqueta es una palabra clave o categoría que se puede asociar a productos
    para describir características como "descuento", "nuevo", "innovativo", etc.

    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_comment=_("Identificador único de la Etiqueta."),
        verbose_name=_("ID de la Etiqueta")
    )
    name = models.CharField(
        max_length=100,
        unique=True,
        db_comment=_("Nombre de la Etiqueta (por ejemplo, 'descuento', 'nuevo', 'innovativo')."),
        verbose_name=_("Nombre de la Etiqueta")
    )

    class Meta:
        verbose_name = _("Etiqueta")
        verbose_name_plural = _("Etiquetas")
        db_table = f'"{Schema.core}"."tag"'
        db_table_comment = "Etiqueta: Almacena palabras clave o categorías que se pueden asociar a productos."
        
    def __str__(self):
        return f"{self.name}"