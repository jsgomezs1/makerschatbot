from django.forms import ValidationError
from inventory.models.product import Product
from inventory.models.tag import Tag
from makerschatbot.clases.abstract.audit_mixin import AuditMixin
from makerschatbot.variables.schemas import Schema
from django.utils.translation import gettext_lazy as _ 
from django.db import models
import uuid

class ProductTag(AuditMixin):
    """
    Modelo que representa la relación entre un Producto y una Etiqueta.

    Este modelo actúa como una tabla intermedia para la relación muchos a muchos
    entre Productos y Etiquetas. Permite asociar múltiples etiquetas a un producto
    y múltiples productos a una etiqueta.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_comment=_("Identificador único de la relación Producto-Etiqueta."),
        verbose_name=_("ID de Producto-Etiqueta")
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        db_comment=_("Producto asociado a la etiqueta."),
        verbose_name=_("Producto")
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        db_comment=_("Etiqueta asociada al producto."),
        verbose_name=_("Etiqueta")
    )

    class Meta:
        verbose_name = _("Producto-Etiqueta")
        verbose_name_plural = _("Productos-Etiquetas")
        db_table = f'"{Schema.core}"."product_tag"'
        db_table_comment = "Producto-Etiqueta: Tabla intermedia para la relación muchos a muchos entre Productos y Etiquetas."
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'tag'],
                name='unique_toghether_product_tag',
            ),
        ]


    def __str__(self):
        return f"Producto: {self.product.name}, Etiqueta: {self.tag.name}"