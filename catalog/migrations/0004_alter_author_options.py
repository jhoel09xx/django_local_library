# Generated by Django 3.2.9 on 2021-11-28 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('credel', 'CUD opcion'),)},
        ),
    ]
