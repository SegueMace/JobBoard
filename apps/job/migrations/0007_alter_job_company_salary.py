# Generated by Django 3.2.5 on 2021-09-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_auto_20210916_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company_salary',
            field=models.CharField(choices=[('moins_de_5oo', 'moins_de_5oo'), (-500, '500-1000'), (-500, '1000-1500'), (-500, '2000-2500'), (-500, '2500-3000'), (3000, '3000+')], default=-500, max_length=20),
        ),
    ]
