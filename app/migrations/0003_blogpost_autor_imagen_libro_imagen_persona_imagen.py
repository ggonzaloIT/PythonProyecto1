# Generated by Django 5.1.4 on 2025-01-30 21:23

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_model3_autor_rename_model2_libro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('fecha_publicacion', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='autor',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='persona',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
