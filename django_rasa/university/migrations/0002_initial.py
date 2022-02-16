# Generated by Django 4.0.2 on 2022-02-16 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("university", "0001_initial"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="class",
            name="lecturer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="user.lecturer",
                verbose_name="lecturer",
            ),
        ),
        migrations.AddField(
            model_name="branche",
            name="faculty",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="university.faculty",
                verbose_name="faculty",
            ),
        ),
    ]