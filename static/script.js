
function getEmailInputValue(){
    const emailInput = document.getElementById('user-email').value;
    return emailInput;
}

document.getElementById('submit-button').addEventListener('click', () => {
    const email_input = document.getElementById('user-email');
    const email_value = email_input.value;
    
    fetch('/subscribe', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({
        'email': email_value
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        const subscribedUser = document.getElementById("subscribed-or-alreadysubscribed");
        subscribedUser.innerHTML = data.message;

        email_input.value = '';
    })
    
    .catch(error => {
        console.error('Error fetching data', error)
    });

});


