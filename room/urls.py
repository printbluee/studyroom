from django.urls import path
from . import views

urlpatterns = [
    path('search',views.search, name="search"), #검색
    path('room/page/<int:pk>', views.room_info, name='room_info'), #글상세페이지

    path('room/', views.room_add, name='room_add'), # 글추가
    path('room/edit/<int:pk>',views.room_edit, name="room_edit"), #글수정
    path('room/delete/<int:pk>',views.room_delete, name='room_delete'), #글삭제
    
]