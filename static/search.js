const searching = document.getElementById('datatable-search-input');

const sendSearchData = (search)=>{
    const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    $.ajax({
        type:'POST',
        beforeSend: function(xhr , settings){
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
        // url:'search/',
        url:`${window.location.origin + '/home/' + 'search/'}`,
        data:{
            'search': search
        },
        success:(res)=>{
            data = res.data;
            if(Array.isArray(data) && data.length > 0){
                let element = document.getElementById('search_res');
                element.style.display = 'flex';
                element.innerHTML=''
                data.forEach(user =>{
                    document.getElementById('search_res').innerHTML += `
                    <div class='list-group-item'>
                        <a href='${window.location.origin+'/otheruser/' + user.pk }'> 
                            <img src="${user.img}" alt="${user.img}" class="rounded-circle" style="width:30px;height: 30px;margin:5px">
                            <span>${user.first_name}</span>
                            <span>${user.last_name}</span>
                        </a>
                    </div><hr>
                     `
                })
            }
            if(data.length==0){
                let element = document.getElementById('search_res');
                element.style.display = 'none';
            }
        },
        error:(err)=>{
            let element = document.getElementById('search_res');
            element.style.display = 'none';
        }
    })
}

searching.addEventListener('keyup', e=>{
    sendSearchData(e.target.value)
})

