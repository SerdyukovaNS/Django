# Generated by Django 4.0.3 on 2022-03-28 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_product_descriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='descriptions',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]