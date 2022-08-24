from unicodedata import name
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# 정규표현식
from core.utils import util as custom_util

#모델 가져오기
from .models import User

# 메안페아자
@csrf_exempt
def main(requset):
    return render(requset, 'index.html')

# 가입
@csrf_exempt
def resigter(request):
    if request.method == 'POST':
        res_data = {}

        username = request.POST['username'] # 아이디
        nickname = request.POST['nickname'] # 닉네임
        name = request.POST['name'] # 이름
        password = request.POST['password'] # 1차 비밀번호 
        re_password = request.POST['re_password'] # 2차 비밀번호

        if (username and nickname and name and password == re_password): # 2차 비밀번호까지 같을 때
            if custom_util.chk_id(username) and custom_util.chk_nickname(nickname) and custom_util.chk_name(name) and custom_util.chk_password(password):
                user_check = User.objects.filter(username=username)
                user_nickname_check = User.objects.filter(nickname=nickname)
                if user_check: # 회원가 이미 가입되어있음
                    res_data['error'] = "중복된 아이디 입니다"
                elif user_nickname_check:
                    res_data['error'] = "중복된 닉네임 입니다"
                else:
                    user = User.objects.create_user( 
                        username=username,
                        nickname=nickname,
                        name=name,
                        password=password,
                    )
                    login(request, user)
                    return redirect(main)

            elif not custom_util.chk_nickname(nickname):
                res_data['error'] = "닉네임은 4~20자의 영문 대문자,소문자, 특수문자 '_', 숫자 사용 가능합니다."
            elif not custom_util.chk_id(username):
                res_data['error'] = "아이디는 4~20자의 영문 대문자,소문자, 특수문자 '_', 숫자 사용 가능합니다."
            elif not custom_util.chk_password(password):
                res_data['error'] = "비밀번호를 확인하세요. 최소 1개 이상의 소문자, 숫자, 특수문자로 구성되어야 하며 길이는 7자리 이상이어야 합니다."  
            elif not custom_util.chk_name(name):
                res_data['error'] = "이름은 한글과 영문 대 소문자를 사용하세요. (특수기호, 공백 사용 불가) 이름은 2~12자리"
            
            else:
                res_data['error'] = "아이디, 닉네임, 이름, 비밀번호 전부 입력 해주세요"
        else:
            res_data['error'] = "아이디, 닉네임, 이름, 비밀번호 전부 입력 해주세요"

        return render(request, 'resigter.html', res_data) 

    else:
        return render(request, 'resigter.html')


#마이페이지
@login_required
def mypage(request):
    user = request.user

    res_data = {}
    res_data['user'] = {
        'user_id' : user.username, # 회원아이디
        'user_nickname' : user.nickname, # 닉네임
        'user_name' : user.name, # 닉네임
        'user_bio' : user.bio, # 자기소개
    }

    return render(request, 'mypage.html',res_data)

#마이페이지 수정
@login_required
def mypage_edit(request):
    res_data = {}
    user = request.user

    res_data['user'] = {
        'user_id' : user.username, # 회원아이디
        'user_nickname' : user.nickname, # 닉네임
        'user_name' : user.name, # 닉네임
        'user_bio' : user.bio, # 자기소개
    }

    if request.method == 'POST':
        user_bio = request.POST['user_bio']
        user.bio = user_bio
        user.save()
        return redirect('mypage')
    else:
        return render(request, 'mypage_edit.html', res_data)