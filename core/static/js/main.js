const settingIcon = document.querySelectorAll(".setting_icon");
const settingModal = document.querySelectorAll(".setting_icon-modal");
const roomModify = document.querySelectorAll(".room_modify");
const roomRemove = document.querySelectorAll(".room_remove");

for (let i = 0; i < settingIcon.length; i++) {

    settingIcon[i].addEventListener("click", function(){
        settingModal[i].classList.toggle("ds_block");
    })
}

// 세팅 아이콘 클릭시 수정,삭제 버튼 토글

for (let i = 0; i < settingIcon.length; i++) {
    roomRemove[i].addEventListener("click", function(){
       alert("삭제됐습니다.")
    })

}

// 삭제버튼 클릭시 한번더 확인

const mainCon = document.querySelectorAll(".main_con")
const onerProfile = document.querySelectorAll(".oner_box-profile");
const onerSecret = document.querySelectorAll(".oner_box-secret");

for (let i = 0; i < mainCon.length; i++) {

    if(mainCon[i].classList.contains("secret") ) {
        // console.log(i+ "번째있어")
        onerProfile[i].className += " ds-none";
        
    }else {
        onerSecret[i].className += " ds-none";
    }
    
}

// 비밀방일경우 방생성시 .main_con에 secret 클래스가 붙음
// scret클래스가 있을시 열쇠 아이콘 생성