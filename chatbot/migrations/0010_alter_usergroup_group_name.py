# Generated by Django 5.0 on 2024-07-23 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0009_alter_chatting_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='group_name',
            field=models.CharField(choices=[('friends', 'friends'), ('family', 'family'), ('special', 'special'), ('office', 'office'), ('school', 'school'), ('university', 'university'), ('onetoone', 'onetoone'), ('superuser', 'superuser'), ('bhaibrother', 'bhaibrother'), ('atik_group', 'atik_group'), ('mehjabin_group', 'mehjabin_group'), ('group1', 'group1'), ('group2', 'group2'), ('group3', 'group3'), ('group4', 'group4')], max_length=500),
        ),
    ]
