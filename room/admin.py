from django.contrib import admin
from .models import Room_info,Room_group,Room_member,Room_comment

class room_info_Admin(admin.ModelAdmin):
    fields = ['room','room_member','room_comment']
    list_display = ['room', 'room_member', 'room_comment']

class room_group_Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'room_owner', 'room_password', 'create']
    list_display_links = ['id','title']

class room_member_Admin(admin.ModelAdmin):
    list_display = ['join_user', 'group', 'created_at']

class room_comment_Admin(admin.ModelAdmin):
    list_display = ['article', 'comment', 'created_at']

admin.site.register(Room_info,room_info_Admin)
admin.site.register(Room_group,room_group_Admin)
admin.site.register(Room_member,room_member_Admin)
admin.site.register(Room_comment,room_comment_Admin)

