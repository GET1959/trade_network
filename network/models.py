from django.db import models
from django.utils import timezone

NULLABLE = {"blank": True, "null": True}


class Contacts(models.Model):
    email = models.CharField(max_length=50, verbose_name="email")
    country = models.CharField(max_length=100, verbose_name="страна")
    city = models.CharField(max_length=100, verbose_name="город")
    street = models.CharField(max_length=250, verbose_name="улица")
    house_number = models.CharField(max_length=50, verbose_name="номер дома")

    class Meta:
        abstract = True


class NetworkLink(Contacts):
    STATUS = [
        ('factory', 'Завод'),
        ('retailer', 'Розничная сеть'),
        ('enterpriser', 'Индивидуальный предприниматель')
    ]
    name = models.CharField(max_length=100, verbose_name="название")
    status = models.CharField(max_length=60, choices=STATUS, verbose_name='статус звена сети')
    supplier = models.ForeignKey("self", on_delete=models.CASCADE, **NULLABLE, verbose_name="поставщик")
    debt = models.DecimalField(
        default=0.00, max_digits=20, decimal_places=2, verbose_name="Задолженность перед поставщиком"
    )
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"


class Product(models.Model):
    owner = models.ForeignKey(
        NetworkLink, related_name="product", on_delete=models.DO_NOTHING, verbose_name="собственник"
    )
    title = models.CharField(max_length=100, verbose_name="наименование")
    model = models.CharField(max_length=100, verbose_name="модель")
    release_date = models.DateTimeField(default=timezone.now, verbose_name="дата выхода на рынок")

    def __str__(self):
        return f"{self.title}, {self.model}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукция"
