# Generated by Django 4.1 on 2022-09-23 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("room", "0002_room_member"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="room",
            options={"verbose_name": "room list", "verbose_name_plural": "Room list"},
        ),
        migrations.AlterModelOptions(
            name="room_member",
            options={
                "verbose_name": "room join_user_list",
                "verbose_name_plural": "room join_user_list",
            },
        ),
        migrations.CreateModel(
            name="Room_comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.TextField(max_length=200, verbose_name="댓글 내용")),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="작성일"
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="room.room",
                        verbose_name="room 정보",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "room comment",
                "verbose_name_plural": "room comment",
                "db_table": "Room_comment",
            },
        ),
    ]
