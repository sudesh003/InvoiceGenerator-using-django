# Generated by Django 4.2 on 2023-04-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_delete_billno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billno', models.CharField(max_length=50)),
            ],
        ),
    ]
