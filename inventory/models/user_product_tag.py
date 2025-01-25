from inventory.models.tag import Tag
from django.core.validators import MinValueValidator, MaxValueValidator
from inventory.models.user_product import UserProduct
from makerschatbot.clases.abstract.audit_mixin import AuditMixin
from makerschatbot.variables.schemas import Schema
from django.utils.translation import gettext_lazy as _ 
from django.db import models
import uuid

class UserProductTag(AuditMixin):
    """
    Modelo que representa la relación entre un UserProduct y una Etiqueta.

    Este modelo permite asignar etiquetas a productos que ya están relacionados con un usuario específico.
    El objetivo es personalizar la experiencia del usuario asignando etiquetas como "innovative", "discount", etc.,
    basándose en las preferencias o comportamientos del usuario.

    Atributos:
        id (UUIDField): Identificador único de la relación UserProduct-Etiqueta.
        userProduct (ForeignKey): UserProduct asociado a la etiqueta.
        tag (ForeignKey): Etiqueta asociada al UserProduct.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_comment=_("Identificador único de la relación UserProduct-Etiqueta."),
        verbose_name=_("ID de UserProduct-Etiqueta")
    )
    userProduct = models.ForeignKey(
        UserProduct, 
        on_delete=models.CASCADE,
        db_comment=_("UserProduct asociado a la etiqueta."),
        verbose_name=_("UserProduct")
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        db_comment=_("Etiqueta asociada al UserProduct."),
        verbose_name=_("Etiqueta")
    )
    rating = models.DecimalField(
        max_digits=5,  # Total digits, including decimals
        decimal_places=2,  # Number of decimal places
        validators=[
            MinValueValidator(0.00, _('La calificación mínima es 0.00 (Sin impacto)')),
            MaxValueValidator(100.00, _('La calificación máxima es 100.00 (Máximo impacto)'))
        ],
        db_comment=_("Calificación que determina el impacto de la etiqueta en el producto para el usuario."),
        verbose_name=_("Calificación de Impacto")
    )

    class Meta:
        verbose_name = _("UserProduct-Etiqueta")
        verbose_name_plural = _("UserProducts-Etiquetas")
        db_table = f'"{Schema.inventory}"."user_product_tag"'
        db_table_comment = "UserProduct-Etiqueta: Tabla intermedia para la relación muchos a muchos entre UserProducts y Etiquetas."
        constraints = [
            # Garantizar unicidad de la combinación UserProduct y Tag
            models.UniqueConstraint(
                fields=['userProduct', 'tag'],
                name='unique_together_userproduct_tag',
            ),
        ]

    def __str__(self):

        return f"UserProduct: {self.userProduct.id}, Etiqueta: {self.tag.name}"