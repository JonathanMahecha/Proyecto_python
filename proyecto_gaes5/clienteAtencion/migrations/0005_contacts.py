# Generated by Django 4.2.7 on 2023-11-14 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clienteAtencion', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
                'db_table': 'contacts',
                'ordering': ['id'],
            },
        ),
    ]