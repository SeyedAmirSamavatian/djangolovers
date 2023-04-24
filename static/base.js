
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
    post_id = JSON.parse(post_id)
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







// <button class="like-button" data-post-id="{{ post.id }}" data-liked="{{ user in post.likes.all }}">{{ post.likes.count }} Likes</button>

// document.addEventListener("DOMContentLoaded", function() {
//     const likeButtons = document.querySelectorAll('.like-button');
//     console.log('object')
//     likeButtons.forEach(button => {
//         console.log('button')
//         button.addEventListener('click', function(e) {
//             // e.preventDefault();
//             const post_id = this.getAttribute('data-post-id');
//             console.log(post_id);
//             let liked = JSON.parse(this.getAttribute('data-liked'));
//             console.log(liked);
//             const url = '/like-post/' + post_id + '/';
//             console.log(url);
//             const csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
//             console.log(csrf_token);
//             const xhr = new XMLHttpRequest();
//             xhr.open('POST', url);
//             xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
//             xhr.setRequestHeader('X-CSRFToken', csrf_token);
//             xhr.onload = function() {
//                 if (xhr.status === 200) {
//                     const data = JSON.parse(xhr.responseText);
//                     if (data.success) {
//                         liked = !liked;
//                         button.setAttribute('data-liked', liked);
//                         button.textContent = data.likes_count + ' Likes';
//                     }
//                 }
//             };
//             xhr.send('liked=' + liked);
//         });
//     });
// });