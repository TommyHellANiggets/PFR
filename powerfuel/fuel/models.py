from django.db import models

class Fuel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo_url = models.URLField(blank=True)  # Используем URLField для сохранения URL изображения

    def __str__(self):
        return self.name


class CartItem(models.Model):
    # Определите поля вашей модели CartItem здесь
    # Например:
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.names