# Generated by Django 5.0 on 2024-07-23 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0008_alter_chatting_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatting',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
    ]
