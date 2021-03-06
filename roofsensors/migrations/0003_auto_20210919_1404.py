# Generated by Django 3.2.7 on 2021-09-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roofsensors', '0002_auto_20210919_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambientdata',
            name='red_one_humidity',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='ambientdata',
            name='red_one_illumination',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ambientdata',
            name='red_one_temperature',
            field=models.DecimalField(decimal_places=4, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='ambientdata',
            name='red_three_humidity',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='ambientdata',
            name='red_three_illumination',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ambientdata',
            name='red_three_temperature',
            field=models.DecimalField(decimal_places=4, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='ambientdata',
            name='red_two_humidity',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='ambientdata',
            name='red_two_illumination',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ambientdata',
            name='red_two_temperature',
            field=models.DecimalField(decimal_places=4, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='experimentdata',
            name='control_bottom',
            field=models.DecimalField(decimal_places=4, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='experimentdata',
            name='control_top',
            field=models.DecimalField(decimal_places=4, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='experimentdata',
            name='green_roof_bottom',
            field=models.DecimalField(decimal_places=4, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='experimentdata',
            name='green_roof_middle',
            field=models.DecimalField(decimal_places=4, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='experimentdata',
            name='green_roof_top',
            field=models.DecimalField(decimal_places=4, max_digits=5, null=True),
        ),
    ]
