import re

def chk_id(id):
    result = True
    reg = r'^[A-Za-z0-9_]{4,20}$'
    if not re.search(reg, id):
        # print('아이디는 4~20자의 영문 대문자,소문자, 특수문자 '_', 숫자 사용 가능합니다.')
        result = False
    return result

def chk_nickname(nickname):
    result = True
    reg = r'^[A-Za-z가-힣0-9_]{2,12}$'
    if not re.search(reg, nickname):
        result = False
        #print('닉네임은 2자리 이상 12자리 이하이어야 합니다. (특수기호, 공백 사용 불가)')
    return result

def chk_password(pwd):
    result = True
    reg = r'^(?=.*[\d])(?=.*[a-z])(?=.*[!@#$%^&*()])[\w\d!@#$%^&*()]{7,}$'
    if not re.search(reg, pwd):
        # print('비밀번호를 확인하세요. 최소 1개 이상의 소문자, 숫자, 특수문자로 구성되어야 하며 길이는 7자리 이상이어야 합니다.')
        result = False
    return result

def chk_name(name):
    result = True
    reg = r'^[A-Za-z가-힣]{2,10}$'
    if not re.search(reg, name):
        # print("한글과 영문 대 소문자를 사용하세요. (특수기호, 공백 사용 불가)")
        result = False
    return result


# id = "Aa_12"
# pwd = "aa4545!"
# nickname = "혜blue"
# name = "진혜정"

# print(chk_id(id))
# print(chk_password(pwd))
# print(chk_nickname(nickname))
# print(chk_name(name))
