# Generated by Django 4.1 on 2022-09-27 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("room", "0026_room_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="room_comment",
            field=models.ManyToManyField(to="room.room_comment", verbose_name="댓글"),
        ),
    ]
