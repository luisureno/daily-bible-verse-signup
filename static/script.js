



function getEmailInputValue(){
    const emailInput = document.getElementById('user-email').value;
    //console.log(emailInput)
    return emailInput;
    //console.log(emailInput)
}

//const amenAndSend = document.getElementById('submit-button')

document.getElementById('submit-button').addEventListener('click', () => {
    email_input = getEmailInputValue();

    fetch('/subscribe', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({
        'email': email_input
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        const subscribedUser = document.getElementById("subscribed");
        subscribedUser.innerHTML = data.message;
    })
    .catch(error => {
        console.error('Error fetching data', error)
    });

});


