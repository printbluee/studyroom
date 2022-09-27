from django.contrib import admin
from .models import Room,Room_member,Room_comment

class room_Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'room_owner' , 'create']
    list_display_links = ['id', 'title']

class room_member_Admin(admin.ModelAdmin):
    list_display = ['join_user', 'date_joined']

class Room_comment_Admin(admin.ModelAdmin):
    list_display = ['article', 'comment', 'created_at']

admin.site.register(Room,room_Admin)
admin.site.register(Room_member,room_member_Admin)
admin.site.register(Room_comment,Room_comment_Admin)

