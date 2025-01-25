from django.forms import ValidationError
from makerschatbot.clases.abstract.audit_mixin import AuditMixin
from makerschatbot.variables.schemas import Schema
from django.utils.translation import gettext_lazy as _ 
from django.db import models
import uuid

class Stakeholder(AuditMixin):
    """
    Tercero

    Un Stakeholder(Tercero) es una entidad legal, como una empresa, organización o individuo,
    que participa en actividades comerciales o de negocios. 
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_comment=_("Identificador único de la Tercero."),
        verbose_name=_("ID de la Tercero")
    )
    name = models.CharField(
        db_comment=_("Nombre legal de la Tercero."),
        verbose_name=_("Nombre de la Tercero")
    )

    class Meta:
        verbose_name = _("Tercero")
        verbose_name_plural = _("Terceros")
        db_table = f'"{Schema.core}"."stakeholder"'
        db_table_comment = "Tercero: Un Stakeholder(Tercero) es una entidad legal, como una empresa, organización o individuo, que participa en actividades comerciales o de negocios. "
        
    def __str__(self):
        return f"{self.name} ({self.id})"