# Generated by Django 4.0.4 on 2022-05-23 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('category', models.TextField(choices=[('GRC', 'grocery'), ('STA', 'stationery'), ('HUS', 'house hold')])),
            ],
        ),
    ]
