# Generated by Django 4.1 on 2022-09-24 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("room", "0006_alter_room_member_join_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room_member",
            name="join_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="가입자",
            ),
        ),
    ]
