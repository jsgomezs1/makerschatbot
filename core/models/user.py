from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from makerschatbot.variables.schemas import Schema

class User(models.Model):
    """
    Modelo que representa a un usuario en el sistema.

    Un usuario es una persona que interactúa con el Ecommerce y tiene credenciales
    de autenticación para acceder al sistema.

    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("ID de Usuario"),
        db_comment=_("Identificador único para el usuario.")
    )
    name = models.CharField(
        unique=True,
        verbose_name=_("Nombre de Usuario"),
        db_comment=_("Nombre de usuario para inicio de sesión.")
    )
    image = models.URLField(
        blank=True,
        verbose_name=_("Imagen de Perfil"),
        db_comment=_("Imagen o foto de perfil del usuario. Formatos aceptados: JPG, PNG."),
    )
    email = models.EmailField(
        null=True,
        verbose_name=_("Correo Electrónico"),
        db_comment=_("Dirección de correo electrónico para inicio de sesión.")
    )
    phone = models.CharField(
        null=True,
        verbose_name=_("Teléfono"),
        db_comment=_("Número de teléfono para inicio de sesión.")
    )
    password = models.CharField(
        null=True,
        verbose_name=_("Contraseña"),
        db_comment=_("Contraseña encriptada o hasheada.")
    )
    active = models.BooleanField(
        default=True,
        verbose_name=_("Activo"),
        db_comment=_("Indica si la cuenta de usuario está activa.")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Creado en"),
        db_comment=_("Fecha y hora de creación de este registro.")
    )

    class Meta:
        verbose_name = _("Usuario")
        verbose_name_plural = _("Usuarios")
        db_table = f'"{Schema.core}"."user"'
        
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['email']),
            models.Index(fields=['phone']),
        ]

    def __str__(self):
        return f"{self.name} ({self.id})"