# Generated by Django 4.2.4 on 2023-08-21 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_api_key_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='api_key',
            field=models.CharField(default='r4qDcJfejlt4etL1SlRXkkHz7I0R19QdlVtCsVPqvJA', editable=False, max_length=500, unique=True),
        ),
    ]