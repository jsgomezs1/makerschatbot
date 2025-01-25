from django.forms import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models.user import User
from inventory.models.product import Product
from makerschatbot.clases.abstract.audit_mixin import AuditMixin
from makerschatbot.variables.schemas import Schema
from django.utils.translation import gettext_lazy as _ 
from django.db import models
import uuid

class UserProduct(AuditMixin):
    """
    Modelo que representa un Producto personalizado para un Usuario.

    Este modelo almacena un precio diferenciado para un producto específico para un usuario,
    permitiendo la aplicación de discriminación de precios. También incluye una calificación
    de recomendación que predice cuánto le gustará el producto al usuario.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_comment=_("Identificador único del registro de UserProduct."),
        verbose_name=_("ID de UserProduct")
    )
    product = models.ForeignKey(
        Product,  
        on_delete=models.PROTECT,
        db_comment=_("Producto al que se aplica el precio diferenciado."),
        verbose_name=_("Producto")
    )
    user = models.ForeignKey(
        User,  
        on_delete=models.PROTECT,
        db_comment=_("Usuario al que se aplica el precio diferenciado."),
        verbose_name=_("Usuario")
    )
    price = models.DecimalField(
        max_digits=10,  
        decimal_places=2,
        db_comment=_("Precio diferenciado del producto para el usuario."),
        verbose_name=_("Precio")
    )
    recommendation_rating = models.DecimalField(
        max_digits=5,  
        decimal_places=2,
        validators=[
            MinValueValidator(0.00, _('La calificación mínima es 0.00 (Muy mal)')),
            MaxValueValidator(100.00, _('La calificación máxima es 100.00 (Excelente)'))
        ],
        db_comment=_("Calificación de recomendación del producto para el usuario. "
                    "Debe ser un valor decimal entre 0.00 (Muy mal) y 100.00 (Excelente)."),
        verbose_name=_("Calificación de Recomendación")
    )

    class Meta:
        verbose_name = _("Producto de Usuario")
        verbose_name_plural = _("Productos de Usuario")
        db_table = f'"{Schema.inventory}"."user_product"'
        db_table_comment = "Producto de Usuario: Almacena un precio diferenciado y una calificación de recomendación para un producto específico para un usuario."
        unique_together = (("product", "user"),)  # Ensure each product-user combination is unique

    def __str__(self):

        return f"Usuario: {self.user.name}, Producto: {self.product.name}"