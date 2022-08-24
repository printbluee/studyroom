from django.db import models
from core.models import User
import uuid

class Room(models.Model):
    title = models.CharField(max_length=50, verbose_name="제목") #제목
    sub_title = models.CharField(max_length=100, blank=True, verbose_name="부제목") #부제목
    content = models.TextField(verbose_name="내용") #콘텐츠
    create = models.DateTimeField(verbose_name='작성일', auto_now_add=True) #작성일

    room_owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="방장") #방장
    room_password = models.CharField(max_length=5, blank=True, verbose_name="방비밀번호") #방비밀번호

    updated = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)

    
    def __str__(self):
        return f'[{self.id}] {self.title} {self.room_owner} {self.room_password}/ {self.create}' # id=id
    
    def get_absolute_url(self): #어드민에서 게시글 바로 볼 수 있음
        return f'room/page/{self.id}'

    class Meta:
        verbose_name = "room 목록"
        verbose_name_plural = "room 목록"