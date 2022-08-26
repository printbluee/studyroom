from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

#모델 가져오기
from room.models import Room

#글쓰기추가  
@login_required
def room_add(request):
    if request.method == 'POST': # post요청일 경우 if문 실행
        title = request.POST.get('title', None)
        sub_title = request.POST.get('sub_title', None)
        content = request.POST.get('content', None) 
        room_password = request.POST.get('room_password', None) 
        room_owner = request.user 

        if not title:
            return render(request, 'room_add.html', {"error" : "방제목를 입력 해주세요."}) 
            
        if not sub_title:
            return render(request, 'room_add.html', {"error" : "부제목을 입력 해주세요"}) 

        if not content:
            return render(request, 'room_add.html', {"error" : "내용을 입력 해주세요"})

        if room_password:
            if len(room_password) != 5: # 비밀번호는 필수가 아니지만 있을 경우 숫자 5글자
                return render(request, 'room_add.html', {"error" : "방 비밀번호는 숫자 5글자로 설정해주세요"})

        if (title and sub_title and content):
            PostingObj = Room()
            PostingObj.title = title
            PostingObj.sub_title = sub_title
            PostingObj.content = content
            PostingObj.room_owner = room_owner
            PostingObj.room_password =room_password
            PostingObj.save() # 저장
            return redirect('main') # core/views.py에 main함수 이동(메인페이지)

        else:
            return render(request, 'room_add.html', {"error" : "에러발생 모든 내용을 입력 해주세요"}) 
    else:
        return render(request, 'room_add.html')


