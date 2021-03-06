# Generated by Django 2.2 on 2019-09-09 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import estate.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Negocio')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha edición')),
            ],
            options={
                'verbose_name': 'Negocio',
                'verbose_name_plural': 'Negocios',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('price', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Precio')),
                ('room', models.SmallIntegerField(verbose_name='Habitaciones')),
                ('bathroom', models.SmallIntegerField(verbose_name='Baños')),
                ('area', models.SmallIntegerField(verbose_name='Área')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Teléfono')),
                ('image_cover', models.ImageField(blank=True, null=True, upload_to='image_cover', verbose_name='Imagen Portada')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha edición')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('business', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='estate.Business', verbose_name='Negocio')),
            ],
            options={
                'verbose_name': 'Propiedad',
                'verbose_name_plural': 'Propiedades',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Estructura')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha edición')),
            ],
            options={
                'verbose_name': 'Estructura',
                'verbose_name_plural': 'Estructuras',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='EstateImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, upload_to=estate.models.get_image_filename)),
                ('estate', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='estate.Estate')),
            ],
        ),
        migrations.AddField(
            model_name='estate',
            name='structure',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='estate.Structure', verbose_name='Estructura'),
        ),
    ]
