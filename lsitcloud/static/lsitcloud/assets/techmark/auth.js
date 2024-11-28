async function register(event) {
    document.getElementById("message").innerHTML = "OTP Sent on email";
    event.preventDefault();  // Prevent the default form submission
    const form = event.target;
    const formData = new FormData(form);
    try {
        const response = await fetch(registerUrl, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')  // Add CSRF token for Django
            }
        });

        if (response.ok) {
            const data = await response.json();
            if(data["success"]){
                document.getElementById("signupForm").innerHTML = "";
                document.getElementById("otpForm").innerHTML = 
                `<div class="row">
                    <div class="form-group col-xl-12">
                        <label>OTP</label> <input class="form-control" name="otp" placeholder="Enter your otp" type="text">
                    </div>
                </div>
                <button type="submit" class="btn btn-primary btn-block">Confirm</button>
                <p class="text-center mt-3"id="message"></p>`;
            }else{
                document.getElementById("message").innerHTML = data["message"];
            }
        } else {
            const errorData = await response.json();
            console.log(errorData)
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function verifyotp(event) {
    event.preventDefault();  // Prevent the default form submission
    const form = event.target;
    const formData = new FormData(form);
    try {
        const response = await fetch(verifyOtpUrl, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')  // Add CSRF token for Django
            }
        });

        if (response.ok) {
            const data = await response.json();
            if(data["success"]){
                document.getElementById("message").innerHTML = data["message"];
                location = "dashboard";
            }else{
                document.getElementById("message").innerHTML = data["message"];
            }
            form.reset();  // Optionally reset the form fields
        } else {
            const errorData = await response.json();
            console.log(errorData)
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

function logout(){
    // Send a POST request to the Django backend
    fetch(logoutUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie('csrftoken'),
        },
    })
    /*.then(response => {
        if (response.ok) {
            return response.json(); // Parse JSON only if the response is OK
        } else {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
    }).then(data => {
        // Process the data if the response was OK
        document.getElementById("response-message").innerText = data.message;
    }).catch(error => {
        // Handle errors (e.g., non-200 responses)
        console.error("Error:", error);
        document.getElementById("response-message").innerText = "An error occurred.";
    });*/
}

// CSRF Token helper function (for Django)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}