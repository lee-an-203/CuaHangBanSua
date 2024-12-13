var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId', productId, 'action', action)
        console.log('user:', user)
        if (user === "AnonymousUser") {
            console.log('user not logeed in')
        } else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action) {
    console.log('user logged in, success add')
    fetch(/update_item/,{
        method: 'POST',  // Changed "POOT" to "POST"
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            productId: productId,
            action: action
        }),

    })
    .then((response) => {
    response.json()
    })
    .then((data) => {
        console.log('data', data)
    })
    .catch(error => console.error('Error:', error));
}
