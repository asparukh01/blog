let updateButton = $('#post_update')[0];
updateButton.addEventListener('submit', (e) => {
    e.preventDefault()
    let post = $('#button_update').data('post-id')
    let title = $('#button_update').data('post-title')
    let link = $('#button_update').data('post-link')
    let text = $('#button_update').data('post-text')
    let category = $('#button_update').data('post-category')
    let status = $('#button_update').data('post-status')
    let t = document.getElementById('title')
    let l = document.getElementById('link')
    let te = document.getElementById('text')
    let c = document.getElementById('category')
    let s = document.getElementById('status')

    console.log(title)

    $.ajax({
        url: `http://127.0.0.1:8000/api/post/update/${post}/`,
        method: 'PATCH',
        headers: {Authorization: "Token " + localStorage.getItem("apiToken")},
        data: JSON.stringify({
            'title': title,
            'link': link,
            'text': text,
            'category': category,
            'status': status
        }),
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
            t.innerText = data['title']
            l.innerText = data['link']
            te.innerText = data['text']
            c.innerText = data['category']
            s.innerText = data['status']
            window.location.replace(`http://127.0.0.1:8000/post_detail/${post}/`)
        },
        error: function (err) {
            console.log(err);
        }
    });
})