let post_form = document.getElementById('post_form')
post_form.addEventListener('submit', (e) => {
        e.preventDefault()

        let inputImage = $('#image')[0];
        let inputTitle = $('#title')[0];
        let inputLink = $('#link')[0];
        let inputText = $('#text')[0];
        let inputCategory = $('#category')[0];
        let inputStatus = $('#status')[0];


        $.ajax({
                url: 'http://127.0.0.1:8000/api/post/create/',
                method: 'post',
                headers: {'Authorization': `Token ${localStorage.apiToken}`},
                data: JSON.stringify({
                    "title": inputTitle.value,
                    "link": inputLink.value,
                    "text": inputText.value,
                    "category": inputCategory.value,
                    "status": inputStatus.value
                }),
                dataType: 'json',
                contentType: 'application/json',
                success: (data) => {
                    console.log(data)
                    window.location.replace('http://127.0.0.1:8000/')
                },
                error: function (err) {
                    console.log(err)
                }
            }
        )
    }
)


