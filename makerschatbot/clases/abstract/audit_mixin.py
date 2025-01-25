from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from core.models.user import User


class AuditMixin(models.Model):
    """
    Mixin de Auditoría.

    Un mixin de auditoría proporciona campos de usuario y fecha-hora para rastrear la creación, actualización y
    eliminación lógica de registros.
    """

    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_created",
        verbose_name=_("Creado por"),
        db_comment=_("Usuario que creó este registro.")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Creado en"),
        db_comment=_("Fecha y hora de creación de este registro.")
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        related_name="%(app_label)s_%(class)s_updated",
        verbose_name=_("Actualizado por"),
        db_comment=_("Usuario que actualizó por última vez este registro.")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null= True,
        verbose_name=_("Actualizado en"),
        db_comment=_("Fecha y hora de la última actualización de este registro.")
    )
    deleted_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        related_name="%(app_label)s_%(class)s_deleted",
        verbose_name=_("Eliminado por"),
        db_comment=_("Usuario que realizó la eliminación lógica de este registro.")
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Eliminado en"),
        db_comment=_("Fecha y hora de la eliminación lógica de este registro.")
    )
    audit_status = models.CharField(
        max_length=1,
        choices=[
            ('C', _('Created')),
            ('U', _('Updated')),
            ('D', _('Deleted')),
        ],
        default='C',
        verbose_name=_("Estado de Auditoría"),
        db_comment=_("Estado del registro (Creado, Actualizado, Eliminado).")
    )

    class Meta:
        abstract = True
