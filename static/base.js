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
        $.ajax({
            url:  `${window.location.origin}/home/${comment_id}/delete/`,
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



function follow(){
    const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        $.ajax({
            url:  window.location.href+"follow/",
            type: 'POST',
            beforeSend: function(xhr , settings){
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            },
            data: {},
            success: function(response) {
                if (response.success) {
                    $('#follow_btn').html(response.follow);
                }
            },
            error: function() {
                alert('An error occurred while following.');
            }
        });
}

function sendMessage(user_id){
    const form = document.querySelector('#send-message-form');
    const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const formData = new FormData(form);
    fetch(`${window.location.origin}/chat/${user_id}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            $('#message_textarea').val('');
            alert(data.alert)
            let close = $('#close_modal').click() 
            }
        })

}


function send_chat(){
    const form = document.querySelector('#sendChatText');
    const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const formData = new FormData(form);
    fetch(`/chat/send/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            $('#sendChatInput').val('');
            }
        })
}


function deleteChat(id){
    const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        $.ajax({
            url: '/chat/delete/'+ id+'/' ,
            type: 'POST',
            beforeSend: function(xhr , settings){
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            },
            data: {},
            success: function(response) {
                if (response.success) {
                    alert("پیام مورد نظر حذف شد");
                }
            },
            error: function() {
                alert('حذف پیام با مشکل روبرو شد! دوباره امتحان کنید');
            }
        });
} 


function onlineUser(){
    const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        $.ajax({
            url: `${window.location.origin + '/onlines/'}`,
            type: 'POST',
            beforeSend: function(xhr , settings){
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            },
            data: {},
            success: function(response) {
                if (response.success) {
                    console.log(response.dataOnline)
                    element = document.querySelector('#onlineUsers');
                    if(element){
                        element.innerHTML='';
                        data =response.dataOnline;
                        data.forEach(user =>{
                            element.innerHTML += ` 
                                    <a href='${window.location.origin+'/otheruser/' + user.id }' class='position-relative' title='${user.first_name + ' ' + user.last_name}'>
                                       <img src="${user.image}" alt="${user.first_name + ' ' + user.last_name}" class="rounded-circle" style="width:50px;height:50px;margin:2px;border:solid 3px #0ff19d">
                                    </a>
                            `;
                        })

                    }
                }
            },
            error: function() {
                console.log('error')
            }
        });
} 
