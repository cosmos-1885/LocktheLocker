# Generated by Django 4.2.1 on 2023-06-04 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("locker", "0003_rename_application_appointment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="locker",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="locker.locker",
            ),
        ),
    ]
