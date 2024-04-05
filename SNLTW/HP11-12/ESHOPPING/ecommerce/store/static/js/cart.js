var btns = document.getElementsByClassName('addtocart')

for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        location.reload()

        if (user === "AnonymousUser") {
            alert("User is not logged in")
        } else {
            updateCart(productId, action)
        }
    })
}

const updateCart = (id, action) => {
    let url = "/updatecart"
    fetch(url, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({"productId": id, "action": action})
    })
    
    .then(response => response.json())
    .then(data => console.log(data))
}