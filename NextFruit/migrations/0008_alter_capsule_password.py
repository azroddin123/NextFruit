# Generated by Django 3.2 on 2022-05-17 05:10

from django.db import migrations, models



class Migration(migrations.Migration):

    dependencies = [
        ('NextFruit', '0007_auto_20220517_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capsule',
            name='password',
            field=models.CharField(blank=True,max_length=100, null=True),
        ),
    ]
