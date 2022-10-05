from tokenize import group
from django.db import models
from core.models import User
import uuid
from django.utils import timezone
from django.conf import settings

class Room_group(models.Model):
    room_owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="G_room_owner") #방장
    title = models.CharField(max_length=50, verbose_name="G_title") #제목
    sub_title = models.CharField(max_length=100, blank=True, verbose_name="G_subtitle") #부제목
    content = models.TextField(verbose_name="G_content") #콘텐츠
    create = models.DateTimeField(verbose_name='G_create', auto_now_add=True) #작성일
    room_password = models.CharField(max_length=5, blank=True, verbose_name="G_roompassword") #방비밀번호
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        # return self.title
        return f'[{self.pk}] {self.title} {self.room_owner} {self.room_password}/ {self.create}' # id=id

    def get_absolute_url(self): #어드민에서 게시글 바로 볼 수 있음
        return f'room/page/{self.pk}'

    class Meta:
        verbose_name = "group "
        verbose_name_plural = "Group"

class Room_member(models.Model):
    join_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, verbose_name="M_joinuser")
    group = models.ForeignKey(Room_group, on_delete=models.CASCADE, verbose_name="M_group")
    created_at = models.DateField(default=timezone.now, verbose_name="M_created")

    def __str__(self):
        return f'{self.join_user}'

    class Meta:
        db_table = 'room_member'
        verbose_name = "Member"

class Room_comment(models.Model):
    group = models.ForeignKey(Room_group, on_delete=models.CASCADE, verbose_name="C_group")
    article = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="C_article")    
    comment = models.TextField(max_length=200, verbose_name="C_comment")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="C_created")

    def __str__(self):
        return f'{self.article} {self.comment}'

    class Meta:
        db_table = 'room_comment'
        verbose_name = "Comment"

class Room_info(models.Model):
    room = models.ForeignKey(Room_group, on_delete=models.CASCADE, verbose_name="info_room")
    room_member = models.ForeignKey(Room_member,on_delete=models.CASCADE,  blank=True, verbose_name="info_room_member")
    room_comment = models.ForeignKey(Room_comment,on_delete=models.CASCADE,  blank=True, verbose_name="info_room_comment") #댓글

    def __str__(self):
        return f'{self.room_member}'

    def get_absolute_url(self): #어드민에서 게시글 바로 볼 수 있음
        return f'room/page/{self.pk}'

    class Meta:
        verbose_name = "Room info"
        verbose_name_plural = "Room info"