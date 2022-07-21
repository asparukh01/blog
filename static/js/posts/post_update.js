let button_update = $('#button_update')[0];
button_update.addEventListener('click', (e) => {
    e.preventDefault()
    let post = $('#button_update').data('post-id')
    let title = document.getElementById('title')
    let image = document.getElementById('image')
    let link = document.getElementById('link')
    let text = document.getElementById('text')
    let category = document.getElementById('category')
    let status = document.getElementById('status')

    $.ajax({
        url: `http://127.0.0.1:8000/api/post/update/${post}/`,
        method: 'PATCH',
        headers: {
            Authorization: "Token " + localStorage.getItem("apiToken"),
        },
        data: JSON.stringify({
            'image':image.value,
        }),
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
            console.log(data)
            window.location.replace('http://127.0.0.1:8000/')
        },
        error: function (err) {
            console.log(err);
        }
    });
})