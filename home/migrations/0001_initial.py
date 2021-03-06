# Generated by Django 3.0.8 on 2020-07-17 17:17

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=222)),
                ('keywords', models.CharField(max_length=222)),
                ('description', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=222)),
                ('address', models.CharField(blank=True, max_length=222)),
                ('phone', models.CharField(blank=True, max_length=222)),
                ('fax', models.CharField(blank=True, max_length=222)),
                ('email', models.CharField(blank=True, max_length=222)),
                ('smtserver', models.CharField(blank=True, max_length=222)),
                ('smtemail', models.CharField(blank=True, max_length=222)),
                ('smtpassword', models.CharField(blank=True, max_length=222)),
                ('smtport', models.CharField(blank=True, max_length=222)),
                ('icon', models.ImageField(blank=True, upload_to='images/')),
                ('facebook', models.CharField(blank=True, max_length=222)),
                ('instagram', models.CharField(blank=True, max_length=222)),
                ('twitter', models.CharField(blank=True, max_length=222)),
                ('youtube', models.CharField(blank=True, max_length=222)),
                ('telegram', models.CharField(blank=True, max_length=222)),
                ('aboutus', ckeditor_uploader.fields.RichTextUploadingField()),
                ('contact', ckeditor_uploader.fields.RichTextUploadingField()),
                ('references', ckeditor_uploader.fields.RichTextUploadingField()),
                ('status', models.CharField(choices=[('True', 'Mavjud'), ('False', 'Mavjud emas')], max_length=155)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
