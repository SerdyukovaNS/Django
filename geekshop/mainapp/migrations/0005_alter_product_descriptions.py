# Generated by Django 4.0.3 on 2022-03-28 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_product_descriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='descriptions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
