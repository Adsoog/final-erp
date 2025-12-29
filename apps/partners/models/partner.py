from django.db import models
from django.urls import reverse
from django.conf import settings


class Partner(models.Model):
    class DocumentType(models.TextChoices):
        DNI = 'DNI', 'DNI'
        RUC = 'RUC', 'RUC'
        CE = 'CE', 'Carnet de Extranjeria'
        PASSPORT = 'PASSPORT', 'Pasaporte'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='partner', verbose_name="Usuario de Sistema")
    name = models.CharField("Nombre", max_length=255, db_index=True)
    document_type = models.CharField("Tipo Documento", max_length=10, choices=DocumentType.choices, default=DocumentType.RUC)
    document_number = models.CharField("Numero Documento", max_length=20, unique=True)
    email = models.EmailField("Correo Electronico", null=True, blank=True)
    phone = models.CharField("Telefono", max_length=50, null=True, blank=True)
    mobile_phone = models.CharField("Telefono movil", max_length=50, null=True, blank=True)
    address = models.CharField("Direccion", max_length=350, null=True, blank=True)
    website = models.URLField("Pagina Web", blank=True, null=True)
    is_costumer = models.BooleanField("Es Client", default=True)
    is_supplier = models.BooleanField("Es Proveedor", default=False)
    is_costumer = models.BooleanField("Es Trabajador", default=False)
    is_carrier = models.BooleanField("Es Transportista", default=False)
    is_shareholder = models.BooleanField("Es Accionista", default=False)
    is_financial_entity = models.BooleanField("Es Entidad Financiera", default=False)

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = "Partners"
        ordering = ['name']

    def __str__(self):
        return self.name + self.document_number

    def get_absolute_url(self):
        return reverse("Partner_detail", kwargs={"pk": self.pk})
