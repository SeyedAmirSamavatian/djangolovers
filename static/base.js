
const Registery_form_input = document.getElementById('Registery_form_input');
const inputList = Registery_form_input.getElementsByTagName('input');
if(Registery_form_input && inputList){
    for (let i = 0; i < inputList.length; i++) {
        inputList[i].classList.add('form-control');
        inputList[i].style.width = '80%';
    }
}




