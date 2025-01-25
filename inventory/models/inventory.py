from django.forms import ValidationError
from inventory.models.product import Product
from makerschatbot.clases.abstract.audit_mixin import AuditMixin
from makerschatbot.variables.schemas import Schema
from django.utils.translation import gettext_lazy as _ 
from django.db import models
import uuid

class Inventory(AuditMixin):
    """
    Modelo que representa el Inventario de un Producto en el sistema.

    El Inventario almacena la cantidad disponible de un producto específico en stock.
    Está asociado a un Producto y registra la cantidad actual en inventario.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_comment=_("Identificador único del registro de Inventario."),
        verbose_name=_("ID del Inventario")
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        db_comment=_("Producto al que pertenece el registro de Inventario."),
        verbose_name=_("Producto")
    )
    quantity = models.IntegerField(
        db_comment=_("Cantidad disponible del producto en stock."),
        verbose_name=_("Cantidad")
    )

    class Meta:
        verbose_name = _("Inventario")
        verbose_name_plural = _("Inventarios")
        db_table = f'"{Schema.inventory}"."inventory"'
        db_table_comment = "Inventario: Almacena la cantidad disponible de un producto específico en stock."
        
    def __str__(self):
        return f"Producto: {self.product.name}, Cantidad: {self.quantity}"