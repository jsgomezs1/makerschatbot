from django.forms import ValidationError
from inventory.models.brand import Brand
from inventory.models.product_type import ProductType
from makerschatbot.clases.abstract.audit_mixin import AuditMixin
from makerschatbot.variables.schemas import Schema
from django.utils.translation import gettext_lazy as _ 
from django.db import models
import uuid

class Product(models.Model):
    """
    Producto.

    Un Producto es un artículo específico que se vende o distribuye, como una botella de soda
    de una marca en particular. Está asociado a una Marca y a un Tipo de Producto.


    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_comment=_("Identificador único del Producto."),
        verbose_name=_("ID del Producto")
    )
    name = models.CharField(
        max_length=255,
        db_comment=_("Nombre del Producto."),
        verbose_name=_("Nombre del Producto")
    )
    brand = models.ForeignKey(
        Brand, 
        on_delete=models.PROTECT,
        db_comment=_("Marca a la que pertenece el Producto."),
        verbose_name=_("Marca")
    )
    product_type = models.ForeignKey(
        ProductType, 
        on_delete=models.PROTECT,
        db_comment=_("Tipo de Producto al que pertenece el Producto."),
        verbose_name=_("Tipo de Producto")
    )

    class Meta:
        verbose_name = _("Producto")
        verbose_name_plural = _("Productos")
        db_table = f'"{Schema.inventory}"."product"'
        db_table_comment = "Producto: Representa un artículo específico que se vende o distribuye, asociado a una Marca y un Tipo de Producto."
        
    def __str__(self):

        return f"{self.name} ({self.id})"