from django.forms import ValidationError
from core.models.stakeholder import Stakeholder
from makerschatbot.clases.abstract.audit_mixin import AuditMixin
from makerschatbot.variables.schemas import Schema
from django.utils.translation import gettext_lazy as _ 
from django.db import models
import uuid

class Brand(models.Model):
    """
    Marca.

    Una Marca es una identidad comercial que representa un producto, servicio o línea de productos.
    Está asociada a un Stakeholder (Tercero), que es la entidad legal propietaria de la marca.

    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_comment=_("Identificador único de la Marca."),
        verbose_name=_("ID de la Marca")
    )
    name = models.CharField(
        db_comment=_("Nombre de la Marca."),
        verbose_name=_("Nombre de la Marca")
    )
    stakeholder = models.ForeignKey(
        Stakeholder,
        on_delete=models.PROTECT,
        db_comment=_("Stakeholder (Tercero) propietario de la marca."),
        verbose_name=_("Stakeholder")
    )

    class Meta:
        verbose_name = _("Marca")
        verbose_name_plural = _("Marcas")
        db_table = f'"{Schema.inventory}"."brand"'
        db_table_comment = "Marca: Representa una identidad comercial asociada a un Stakeholder (Tercero)."
        
    def __str__(self):
        return f"{self.name} ({self.id})"