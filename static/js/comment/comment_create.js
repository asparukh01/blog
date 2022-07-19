let comment_form = document.getElementById('comment_form')
comment_form.addEventListener('submit', (e) => {
        e.preventDefault()
        let  post = $('#post_id')[0]
        let inputCommentText = $('#comment_text')[0];
        $.ajax({
                url: `http://127.0.0.1:8000/api/post/${post.innerText}/comment/create/`,
                method: 'post',
                headers: {'Authorization': `Token ${localStorage.apiToken}`},
                data: JSON.stringify({
                    "comment_text": inputCommentText.value,
                }),
                dataType: 'json',
                contentType: 'application/json',
                success: (data) => {
                    console.log(data)
                    window.location.replace(`http://127.0.0.1:8000/post_detail/${post.innerText}/`)
                },
                error: function (err) {
                    console.log(err)
                }
            }
        )
    }
)


