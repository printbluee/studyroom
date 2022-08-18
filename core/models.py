from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# 일반 유저와 관리자 생성하는 함수
class UserManager(BaseUserManager):
    def create_user(self, username, nickname, password=None):
        """
        주어진 이름, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not username:
            raise ValueError(('Users must have an username'))

        user = self.model(
            username=username,
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, nickname):
        """
        주어진 이름, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여한다. 
        """
        user = self.create_user(
            username=username,
            password=password,
            nickname=nickname,
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

# 유저 필드 함수
class User(AbstractUser):
    username = models.CharField(max_length=10, blank=False, null=False, unique=True, verbose_name="회원아이디") # 아이디
    nickname = models.CharField(max_length=10, blank=False, null=False, unique=True, verbose_name="닉네임")# 닉네임
    name = models.CharField(max_length=10, blank=False, null=False, verbose_name="회원이름") #이름
    bio = models.TextField(verbose_name='자기소개') # 바이오

    create_at = models.DateTimeField(verbose_name='date joined', auto_now_add=True) # 가입한 날짜
    last_login = models.DateTimeField(verbose_name='last login',auto_now=True) # 마지막 로그인
    
    is_admin =  models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # api_key = models.UUIDField(default=uuid.uuid4)

    object = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'accounts'
        verbose_name = "가입자 목록"
        verbose_name_plural = "가입자 목록"
