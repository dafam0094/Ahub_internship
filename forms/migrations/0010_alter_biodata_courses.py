# Generated by Django 4.2 on 2023-06-29 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0009_alter_biodata_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='courses',
            field=models.CharField(choices=[('SWeb Development', 'Web Development'), ('App Development', 'App Development'), ('Data Science', 'Data Science'), ('Digital Marketing', 'Digital Marketing'), ('Content Management', 'Content Management'), ('UX/UI Design', 'UX/UI Design'), ('Graphic Design', 'Graphic Design'), ('Mentorship', 'Mentorship')], max_length=100),
        ),
    ]
