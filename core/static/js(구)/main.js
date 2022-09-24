const settingIcon = document.querySelectorAll(".setting_icon");
const settingModal = document.querySelectorAll(".setting_icon-modal");
const roomModify = document.querySelectorAll(".room_modify");
const roomRemove = document.querySelectorAll(".room_remove");
const closeModal = document.querySelector(".close-modal");
const ModalExit = document.querySelector(".exit");

for (let i = 0; i < settingIcon.length; i++) {

    settingIcon[i].addEventListener("click", function(){
        settingModal[i].classList.toggle("ds-block");

        
    })
}


// for (let i = 0; i < array.length; i++) {
    
// }
// 세팅 아이콘 클릭시 수정,삭제 버튼 토글

// const closeModal = document.querySelector(".close-modal");
// const ModalExit = document.querySelector(".exit");

//     ModalExit.addEventListener("click", function(){
//         console.log("눌림")
//         closeModal.classList.add("ds_none") ;
//     })

//    function click(){

//    }

// 삭제버튼 클릭시 한번더 확인

const mainCon = document.querySelectorAll(".main_con")
const onerProfile = document.querySelectorAll(".oner_box-profile");
const onerSecret = document.querySelectorAll(".oner_box-secret");

for (let i = 0; i < mainCon.length; i++) {

    if(mainCon[i].classList.contains("secret") ) {
        onerProfile[i].className += " ds-none";   
    }else {
        // onerSecret[i].className += " ds-none";
    }
    
}

// 비밀방일경우 방생성시 .main_con에 secret 클래스가 붙음
// scret클래스가 있을시 열쇠 아이콘 생성


function numberMaxLength(e){
    if(e.value.length > e.maxLength){
        e.value = e.value.slice(0, e.maxLength);
    }
}

// 인풋태그 글자수제한 4글자 
// maxlength로 갯수제어후 스크립트로 제한

// tap
const checkboxBtn = document.querySelector(".create-check-btn");
const checkboxInput = document.querySelector(".password_setting");

    checkboxBtn.addEventListener('click', function(){
		//checked 제어
        // checkboxInput.checked = true;
    if(checkboxInput.checked = true ){
        checkboxInput.classList.toggle("ds-block")
    }else {
        pass;
    }
})


// 비밀번호 입력 체크시 인풋창생성