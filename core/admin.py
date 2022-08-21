from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class AccountAdmin(UserAdmin):
    # 관리자 페이지
    list_display = ('username', 'create_at','last_login','is_admin','is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id','create_at','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User,AccountAdmin)