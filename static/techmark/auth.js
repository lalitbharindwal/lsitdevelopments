async function register(){
    const form = document.getElementById('registerform');
    const fullname = form.fullname.value.trim();
    const email = form.email.value.trim();
    const contactNumber = form.contact_number.value.trim();
    const password = form.password.value;
    const confirmPassword = form.confirm_password.value;
    document.getElementById("message").innerHTML = "OTP Sent on email";

    // Check for missing fields
    if (!fullname || !email || !contactNumber || !password || !confirmPassword) {
        return alert("Missing some fields");
    }

    // Check if passwords match
    if (password !== confirmPassword) {
        return alert("Passwords do not match.");
    }
    // Construct the data object
    const item = {
        "fullname": fullname,
        "email": email,
        "contact-number": contactNumber,
        "password": password,
        "createdon": new Date().toISOString().slice(0, 19).replace("T", " ")
    };

    try {
        const response = await fetch('register', {
            method: 'POST',
            body: JSON.stringify(item),
            headers: {
                'X-CSRFToken': getCookie('csrftoken')  // Add CSRF token for Django
            }
        });

        if (response.ok) {
            const data = await response.json();
            if(data["success"]){
                document.getElementById("registerform").innerHTML = "";
                document.getElementById("otpform").innerHTML = 
                `<div class="mb-3">
                    <label class="mb-1"><strong>OTP</strong></label>
                    <input type="text" id="otp" class="form-control" placeholder="Enter OTP" required>
                </div>
                <div class="text-center">
                    <div class="login-social">
                        <a href="javascript:void(0);" onclick="verifyotp()" class="btn d-block btn-primary light my-3">Verify OTP</a>
                        <p id="message"></p>
                    </div>
                    <div class="mb-3">
                        Already Have account? <a href="techmarklogin">Signin</a>
                    </div>
                </div>`;
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

async function verifyotp(){
    const form = document.getElementById('otpform');
    const otp = form.otp.value.trim();

    // Check for missing fields
    if (!otp) {
        return alert("Missing OTP");
    }

    // Construct the data object
    const item = {
        "otp": otp
    };

    try {
        const response = await fetch('verifyotp', {
            method: 'POST',
            body: JSON.stringify(item),
            headers: {
                'X-CSRFToken': getCookie('csrftoken')  // Add CSRF token for Django
            }
        });

        if (response.ok) {
            const data = await response.json();
            if(data["success"]){
                document.getElementById("message").innerHTML = data["message"];
                location = "techmarklogin";
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

function logout(){
    // Send a POST request to the Django backend
    fetch('logout', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie('csrftoken'),
        },
    })
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