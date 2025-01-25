from django.forms import ValidationError
from makerschatbot.clases.abstract.audit_mixin import AuditMixin
from makerschatbot.variables.schemas import Schema
from django.utils.translation import gettext_lazy as _ 
from django.db import models
import uuid

class ProductType(AuditMixin):
    """
    Modelo que representa un Tipo de Producto en el sistema.

    Un Tipo de Producto es una categoría que agrupa productos similares, como "Sodas", "Jugos", "Snacks", etc.
    Este modelo permite organizar y clasificar productos de diferentes marcas bajo un mismo tipo.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_comment=_("Identificador único del Tipo de Producto."),
        verbose_name=_("ID del Tipo de Producto")
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        db_comment=_("Nombre del Tipo de Producto (por ejemplo, 'Sodas')."),
        verbose_name=_("Nombre del Tipo de Producto")
    )

    class Meta:
        verbose_name = _("Tipo de Producto")
        verbose_name_plural = _("Tipos de Producto")
        db_table = f'"{Schema.inventory}"."product_type"'
        db_table_comment = "Tipo de Producto: Representa una categoría que agrupa productos similares, como 'Sodas' o 'Jugos'."
        
    def __str__(self):

        return f"{self.name} ({self.id})"