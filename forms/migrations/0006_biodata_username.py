# Generated by Django 4.2 on 2023-06-25 14:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_rename_others_name_biodata_other_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]