# Generated by Django 4.1.3 on 2022-11-11 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0004_alter_cook_years_of_experience"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ingredient",
            name="dishes",
        ),
        migrations.AddField(
            model_name="dish",
            name="ingredients",
            field=models.ManyToManyField(
                blank=True, related_name="dishes", to="kitchen.ingredient"
            ),
        ),
        migrations.AlterField(
            model_name="dish",
            name="description",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
