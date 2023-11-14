# Generated by Django 4.2.7 on 2023-11-13 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clienteAtencion', '0003_cite_occupation_typeofservice_worker_delete_article_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headLine', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('cite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clienteAtencion.cite')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'db_table': 'comment',
                'ordering': ['id'],
            },
        ),
    ]