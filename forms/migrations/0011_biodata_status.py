# Generated by Django 4.2 on 2023-07-01 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0010_alter_biodata_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]
