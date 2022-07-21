window.addEventListener('load', (e) => {
    let account = $('#account_id')[0];
    let posts = $('#posts_total')[0];
    let ratin = document.querySelectorAll('p#ratin')
    let lists = []
    for (let i=0; i<ratin.length; i++){
        lists.push(Number(ratin[i].innerText))
    }
    let sum = lists.map(i => x += i, x = 0).reverse()[0]
    if ((sum / posts.innerText) < 3){
        $.ajax({
        url: `http://127.0.0.1:8000/accounts/account/${account.innerText}/karma/`,
        method: 'PATCH',
        headers: {Authorization: "Token " + localStorage.getItem("apiToken")},
        data: JSON.stringify({
            karma: 'Плохая'
        }),
        dataType: "json",
        contentType: "application/json",
        success: (data) => {
                    console.log(data)
                },
        error: function (err) {
            console.log(err);
        }
    });
    }
    else if ((sum / posts.innerText) === 3){
        $.ajax({
        url: `http://127.0.0.1:8000/accounts/account/${account.innerText}/karma/`,
        method: 'PATCH',
        headers: {Authorization: "Token " + localStorage.getItem("apiToken")},
        data: JSON.stringify({
            karma: 'Хорошая'
        }),
        dataType: "json",
        contentType: "application/json",
        success: (data) => {
                    console.log(data)
                },
        error: function (err) {
            console.log(err);
        }
    });
    }
    else if ((sum / posts.innerText) === 5){
        $.ajax({
        url: `http://127.0.0.1:8000/accounts/account/${account.innerText}/karma/`,
        method: 'PATCH',
        headers: {Authorization: "Token " + localStorage.getItem("apiToken")},
        data: JSON.stringify({
            karma: 'Отличная'
        }),
        dataType: "json",
        contentType: "application/json",
        success: (data) => {
                    console.log(data)
                },
        error: function (err) {
            console.log(err);
        }
    });
    }
});