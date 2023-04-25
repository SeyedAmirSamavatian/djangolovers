
const Registery_form_input = document.getElementById('Registery_form_input');
const inputList = Registery_form_input.getElementsByTagName('input');
const textareaList  = Registery_form_input.getElementsByTagName('textarea');
if(Registery_form_input && inputList){
    for (let i = 0; i < inputList.length; i++) {
        inputList[i].classList.add('form-control');
        inputList[i].style.width = '80%';
    }
    for (let i = 0; i < textareaList.length; i++) {
        textareaList[i].classList.add('form-control');
        textareaList[i].style.width = '80%';
    }
}


function likeDislike(post_id){
    const url = '/home/like-post/' + post_id + '/';
    const csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const xhr = new XMLHttpRequest();
    // post_id = JSON.parse(post_id)
    xhr.open('POST', url);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('X-CSRFToken', csrf_token);
    
    xhr.onload = function() {
        if (xhr.status === 200) {
            let response = JSON.parse(xhr.responseText);
            let element = document.getElementById('count'+post_id)
            let count = Number(element.innerHTML)
            element.innerHTML = response.likes_count;
            let image_Liked = document.getElementById('image_Liked'+post_id)
            image_Liked.innerHTML = response.liked_pro;
        }
    }
    xhr.send('post_id=' + post_id);
} 

function SendComment_AJAX(post_id){
    const form = document.querySelector('#comment-form'+post_id);
    const commentsSection = document.querySelector('#comments'+post_id);
    const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const formData = new FormData(form);
    fetch('/home/add_comment/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            formData.forEach((item, index)=>{
                console.log(index+ " " + item)

            });
                commentsSection.innerHTML += 
                `<div id="commentBox${formData.get('comment')}" class="comment d-flex flex-row justify-content-between align-items-center">
                    <div>
                        <small>${formData.get('username')}</small>
                        <p>${formData.get('content')}</p>
                    </div>
                    <ion-icon onclick="DeleteComment({{comment.id}})" style='color:red; cursor: pointer;'; name="trash-outline"></ion-icon>
                </div><hr>`
                ;
            }
        })
} 


function DeleteComment(comment_id){
    const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    console.log(csrftoken)
        $.ajax({
            url:  comment_id + '/delete/',
            type: 'POST',
            beforeSend: function(xhr , settings){
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            },
            data: {},
            success: function(response) {
                if (response.success) {
                    $(`#commentBox${comment_id}` ).remove();
                }
            },
            error: function() {
                alert('An error occurred while deleting the comment.');
            }
        });
} 

