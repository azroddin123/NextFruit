# Generated by Django 3.2 on 2022-05-16 10:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('NextFruit', '0002_alter_capsule_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capsule',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('07f6bd8c-85c8-4547-8532-358fe5d5d99c'), primary_key=True, serialize=False),
        ),
    ]