# Generated by Django 5.1.5 on 2025-01-26 00:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.UUIDField(db_comment='Identificador único de la Tercero.', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID de la Tercero')),
                ('name', models.CharField(db_comment='Nombre legal de la Tercero.', verbose_name='Nombre de la Tercero')),
            ],
            options={
                'verbose_name': 'Tercero',
                'verbose_name_plural': 'Terceros',
                'db_table': '"core"."stakeholder"',
                'db_table_comment': 'Tercero: Un Stakeholder(Tercero) es una entidad legal, como una empresa, organización o individuo, que participa en actividades comerciales o de negocios. ',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(db_comment='Identificador único para el usuario.', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID de Usuario')),
                ('name', models.CharField(db_comment='Nombre de usuario para inicio de sesión.', unique=True, verbose_name='Nombre de Usuario')),
                ('image', models.URLField(blank=True, db_comment='Imagen o foto de perfil del usuario. Formatos aceptados: JPG, PNG.', verbose_name='Imagen de Perfil')),
                ('email', models.EmailField(db_comment='Dirección de correo electrónico para inicio de sesión.', max_length=254, null=True, verbose_name='Correo Electrónico')),
                ('phone', models.CharField(db_comment='Número de teléfono para inicio de sesión.', null=True, verbose_name='Teléfono')),
                ('password', models.CharField(db_comment='Contraseña encriptada o hasheada.', null=True, verbose_name='Contraseña')),
                ('active', models.BooleanField(db_comment='Indica si la cuenta de usuario está activa.', default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_comment='Fecha y hora de creación de este registro.', verbose_name='Creado en')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': '"core"."user"',
                'indexes': [models.Index(fields=['name'], name='user_name_969ffe_idx'), models.Index(fields=['email'], name='user_email_7bbb4c_idx'), models.Index(fields=['phone'], name='user_phone_3acb84_idx')],
            },
        ),
    ]
