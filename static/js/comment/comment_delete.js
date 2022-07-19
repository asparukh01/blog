let delete_comment = document.getElementById('delete_comment')
delete_comment.addEventListener('click', (e) => {
        e.preventDefault()
        let post = $('#post_id')
        console.log(post.innerText)
        let  comment = $('#comment_id')[0]
        $.ajax({
                url: `http://127.0.0.1:8000/api/post/comment/${comment.innerText}/delete/`,
                method: 'delete',
                headers: {'Authorization': `Token ${localStorage.apiToken}`},
                dataType: 'json',
                contentType: 'application/json',
                success: (data) => {
                    console.log(data)
                    window.location.replace(`http://127.0.0.1:8000/`)
                },
                error: function (err) {
                    console.log(err)
                }
            }
        )
    }
)


