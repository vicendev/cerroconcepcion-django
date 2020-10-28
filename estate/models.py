from django.db import models
from django.utils.timezone import now
from django.template.defaultfilters import slugify
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=20, verbose_name="Negocio")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha edición")

    class Meta:
        verbose_name = "Negocio"
        verbose_name_plural = "Negocios"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Structure(models.Model):
    name = models.CharField(max_length=20, verbose_name="Estructura")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha edición")

    class Meta:
        verbose_name = "Estructura"
        verbose_name_plural = "Estructuras"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Estate(models.Model):
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name="Precio")
    room = models.SmallIntegerField(verbose_name="Habitaciones")
    bathroom = models.SmallIntegerField(verbose_name="Baños")
    area = models.SmallIntegerField(verbose_name="Área")
    phone_number = PhoneNumberField(verbose_name="Teléfono", blank=True, null=True)
    business = models.ForeignKey(Business, verbose_name="Negocio", on_delete=models.CASCADE, default=None)
    structure = models.ForeignKey(Structure, verbose_name="Estructura", on_delete=models.CASCADE, default=None)
    image_cover = models.ImageField(verbose_name='Imagen Portada' , upload_to='image_cover', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha edición")

    class Meta:
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"
        ordering = ["-created"]

    def __str__(self):
        return self.title


def get_image_filename(instance, filename):
    title = instance.estate.title
    slug = slugify(title)
    return "estate_images/%s-%s" % (slug, filename)

class EstateImages(models.Model):
    estate = models.ForeignKey(Estate,default=None, on_delete=models.CASCADE,related_name="images")
    file = models.ImageField(upload_to=get_image_filename, blank=True)
