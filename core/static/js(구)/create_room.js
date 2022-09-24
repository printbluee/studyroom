function numberMaxLength(e){
    if(e.value.length > e.maxLength){
        e.value = e.value.slice(0, e.maxLength);
    }
}

// 인풋태그 글자수제한 4글자 
// maxlength로 갯수제어후 스크립트로 제한


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
});

// 비밀번호 입력 체크시 인풋창생성

const fileInput = document.getElementById("fileUpload");

const handleFiles = () => {
  const selectedFile = [...fileInput.files];
  const fileReader = new FileReader();

  fileReader.readAsDataURL(selectedFile[0]);
  fileReader.onload = function () {
    document.getElementById("previewImg").src = fileReader.result;
  };
};

fileInput.addEventListener("change", handleFiles);
