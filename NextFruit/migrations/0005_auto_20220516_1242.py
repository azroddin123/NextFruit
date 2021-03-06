# Generated by Django 3.2 on 2022-05-16 12:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('NextFruit', '0004_auto_20220516_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capsule',
            name='mobile_number',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='capsule',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('495eaa68-0b6d-4b98-a652-da49fc2e2f29'), primary_key=True, serialize=False),
        ),
    ]
