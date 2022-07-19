let one = $('#one')[0];
one.addEventListener('click', (e) => {
    e.preventDefault()
    let post = $('#post_id')[0];
    $.ajax({
        url: `http://127.0.0.1:8000/api/post/${post.innerText}/rating/`,
        method: 'PATCH',
        headers: {Authorization: "Token " + localStorage.getItem("apiToken")},
        data: JSON.stringify({
            rating: 1
        }),
        dataType: "json",
        contentType: "application/json",
        success: (data) => {
                    console.log(data)
                    window.location.reload()
                },
        error: function (err) {
            console.log(err);
        }
    });
});
let two = $('#two')[0];
two.addEventListener('click', (e) => {
    e.preventDefault()
    let post = $('#post_id')[0];
    $.ajax({
        url: `http://127.0.0.1:8000/api/post/${post.innerText}/rating/`,
        method: 'PATCH',
        headers: {Authorization: "Token " + localStorage.getItem("apiToken")},
        data: JSON.stringify({
            rating: 2
        }),
        dataType: "json",
        contentType: "application/json",
        success: (data) => {
                    console.log(data)
                    window.location.reload()
                },
        error: function (err) {
            console.log(err);
        }
    });
});
let three = $('#three')[0];
three.addEventListener('click', (e) => {
    e.preventDefault()
    let post = $('#post_id')[0];
    $.ajax({
        url: `http://127.0.0.1:8000/api/post/${post.innerText}/rating/`,
        method: 'PATCH',
        headers: {Authorization: "Token " + localStorage.getItem("apiToken")},
        data: JSON.stringify({
            rating: 3
        }),
        dataType: "json",
        contentType: "application/json",
        success: (data) => {
                    console.log(data)
                    window.location.reload()
                },
        error: function (err) {
            console.log(err);
        }
    });
});
let four = $('#four')[0];
four.addEventListener('click', (e) => {
    e.preventDefault()
    let post = $('#post_id')[0];
    $.ajax({
        url: `http://127.0.0.1:8000/api/post/${post.innerText}/rating/`,
        method: 'PATCH',
        headers: {Authorization: "Token " + localStorage.getItem("apiToken")},
        data: JSON.stringify({
            rating: 4
        }),
        dataType: "json",
        contentType: "application/json",
        success: (data) => {
                    console.log(data)
                    window.location.reload()
                },
        error: function (err) {
            console.log(err);
        }
    });
});
let five = $('#five')[0];
five.addEventListener('click', (e) => {
    e.preventDefault()
    let post = $('#post_id')[0];
    $.ajax({
        url: `http://127.0.0.1:8000/api/post/${post.innerText}/rating/`,
        method: 'PATCH',
        headers: {Authorization: "Token " + localStorage.getItem("apiToken")},
        data: JSON.stringify({
            rating: 5
        }),
        dataType: "json",
        contentType: "application/json",
        success: (data) => {
                    console.log(data)
                    window.location.reload()
                },
        error: function (err) {
            console.log(err);
        }
    });
});