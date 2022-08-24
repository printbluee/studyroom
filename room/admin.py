from django.contrib import admin
from .models import Room

class room_Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'room_owner' , 'create']
    list_display_links = ['id', 'title']


admin.site.register(Room,room_Admin)
