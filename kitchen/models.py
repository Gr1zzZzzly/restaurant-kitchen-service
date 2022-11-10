from django.db import models
from django.contrib.auth.models import AbstractUser


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.name}"


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()

    class Meta:
        verbose_name = "Cook"
        verbose_name_plural = "Cooks"

    def __str__(self):
        return (
            f"{self.username} "
            f"({self.first_name} {self.last_name}) "
            f"experience: {self.years_of_experience}"
        )


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    dishes = models.ManyToManyField(Dish, related_name="ingredients")

    def __str__(self):
        return self.name
