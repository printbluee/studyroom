from django.db import models
from core.models import User
import uuid
from django.utils import timezone
from django.conf import settings

class Room_comment(models.Model):
    article = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200, verbose_name="댓글 내용")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="작성일")

    def __str__(self):
        return f'{self.article} {self.comment}'
    class Meta:
        db_table = 'room_comment'

class Room_info(models.Model):
    title = models.CharField(max_length=50, verbose_name="제목") #제목
    sub_title = models.CharField(max_length=100, blank=True, verbose_name="부제목") #부제목
    content = models.TextField(verbose_name="내용") #콘텐츠
    create = models.DateTimeField(verbose_name='작성일', auto_now_add=True) #작성일
    room_password = models.CharField(max_length=5, blank=True, verbose_name="방비밀번호") #방비밀번호

    updated = models.DateTimeField(auto_now_add=True) #작성일
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        # return self.title
        return f'[{self.id}] {self.title} {self.room_owner} {self.room_password} {self.room_member}{self.room_comment}/ {self.create}' # id=id

    def get_absolute_url(self): #어드민에서 게시글 바로 볼 수 있음
        return f'room/page/{self.id}'

    class Meta:
        verbose_name = "room"
        verbose_name_plural = "Room 리스트"

class Room(models.Model):
    room = models.ForeignKey(Room_info, on_delete=models.CASCADE, verbose_name="방정보")
    room_owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="방장")
    room_member = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True, verbose_name="유저리스트")
    room_comment = room_comment = models.ManyToManyField(Room_comment, verbose_name="댓글") #댓글

    def get_absolute_url(self): #어드민에서 게시글 바로 볼 수 있음
        return f'room/page/{self.id}'

    class Meta:
        verbose_name = "Room INFO"
        verbose_name_plural = "Room INFO"