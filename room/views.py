import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.utils import timezone
from django.utils.datastructures import MultiValueDictKeyError
#모델 가져오기
from room.models import Room, Room_comment, Room_member

# 글 쓰기
@login_required
def room_add(request):
    if request.method == 'POST':  # post요청일 경우 if문 실행
        title = request.POST.get('title', None)
        sub_title = request.POST.get('sub_title', None)
        content = request.POST.get('content', None)
        room_password = request.POST.get('room_password', None)
        room_owner = request.user

        if not title:
            return render(request, 'create_room.html', {"error": "방제목를 입력 해주세요."})

        if not sub_title:
            return render(request, 'create_room.html', {"error": "부제목을 입력 해주세요"})

        if not content:
            return render(request, 'create_room.html', {"error": "내용을 입력 해주세요"})

        if room_password:
            if len(room_password) != 5:  # 비밀번호는 필수가 아니지만 있을 경우 숫자 5글자
                return render(request, 'create_room.html', {"error": "방 비밀번호는 숫자 5글자로 설정해주세요"})

        if (title and sub_title and content):
            PostingObj = Room()
            PostingObj.title = title
            PostingObj.sub_title = sub_title
            PostingObj.content = content
            PostingObj.room_owner = room_owner
            PostingObj.room_password = room_password
            PostingObj.save()  # 저장
            return redirect('main')  # core/views.py에 main함수 이동(메인페이지)

        else:
            return render(request, 'create_room.html', {"error": "에러발생 모든 내용을 입력 해주세요"})
    else:
        return render(request, 'create_room.html')

# 글 상세페이지
@login_required
def room_info(request, pk):
    article = request.user  # 작성자
    join_user = request.user  # 가입하는 유저

    room_pk = Room.objects.get(pk=pk) # 방함수의 pk
    room_comment = Room_comment.objects.filter(room=pk) # 댓글함수의 room.pk
    room_members = Room_member.objects.filter(group=pk) # 멤버함수의 room.pk

    user_check = Room_member.objects.filter(join_user=request.user)
    
    res_data = {}
    res_data = {
        'room': room_pk,
        'room_comment': room_comment,
        'room_members': room_members,
        'user_check': user_check,
    }

    if request.method == 'POST':
        comment = request.POST.get('comment') # 댓글내용

        try:
            comment = request.POST.get('comment')
        except MultiValueDictKeyError:
            comment = False

        if comment:
            commentobj = Room_comment()
            commentobj.room = room_pk
            commentobj.article = article
            commentobj.comment = comment
            commentobj.created_at = timezone.now()
            commentobj.save()

        elif not room_members: #room 멤버가 아닐때 / 가입과 댓글이 동시에 post로 들어와 제어해줘야함
            memberobj = Room_member()
            memberobj.join_user = join_user
            memberobj.group = room_pk
            memberobj.date_joined = timezone.now()  # 현재시간
            memberobj.save()

    return render(request, 'room_info.html', res_data)


# 검색하기
@csrf_exempt
def search(request):
    search_keyword = request.GET.get('q', None)
    res_data = {}

    if search_keyword:  # 키워드 검색이 들어왔을때만 작동
        if len(search_keyword) > 1:
            room_list = Room.objects.all().order_by('-id')

            search_posting_list = room_list.filter(
                Q(title__icontains=search_keyword) |  # 방제
                Q(sub_title__icontains=search_keyword) |  # 부제
                Q(content__icontains=search_keyword) |  # 내용
                Q(room_owner__username__icontains=search_keyword)  # 방장
            )
            res_data['room'] = search_posting_list
        else:
            res_data['error'] = "검색어는 2글자 이상 입력해주세요."
    else:
        res_data['error'] = "검색 결과가 없습니다."

    return render(request, "index.html", res_data)

# 글 수정
@login_required
def room_edit(request, pk):
    res_data = {}
    try:
        room = Room.objects.get(pk=pk)
    except:
        return render(request, 'room_edit.html', {'error': "잘못된 접근입니다."})

    user = request.user  # 현재 로그인되어있는 유저
    room_owner = room.room_owner  # 포스팅 작성한 유저
    res_data['room_owner'] = room_owner
    if user == room_owner:
        if request.method == 'POST':
            res_data['room'] = room

            title = request.POST['title']
            sub_title = request.POST['sub_title']
            content = request.POST['content']

            if not title:
                res_data['error'] = "제목을 입력 해주세요"
            if not sub_title:
                res_data['error'] = "부제목을 입력 해주세요"
            if not content:
                res_data['error'] = "내용을 입력 해주세요"

            if (title and sub_title and content):  # 모두 입력했을 때
                room.title = title
                room.sub_title = sub_title
                room.content = content
                room.save()  # 저장
                return redirect('main')  # 메인페이지 이동

            else:
                res_data['error'] = "에러발생 모든 내용을 입력 해주세요"

            return render(request, 'room_edit.html', res_data)

        elif request.method == 'GET':
            res_data['room'] = room
            return render(request, 'room_edit.html', res_data)
    else:
        return render(request, 'index.html', {"error": "권한이 없습니다."})

# 글 삭제
@login_required
def room_delete(request, pk):
    room = Room.objects.get(pk=pk)

    if request.method == 'GET':
        room.delete()  # 삭제
        return redirect('main')  # 메인페이지 이동
