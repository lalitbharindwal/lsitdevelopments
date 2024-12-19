function displaycc(){
    document.getElementById("cc").innerHTML = 
    `<h4>Cc: </h4>
    <input type="text" class="form-control bg-transparent" placeholder=" Cc:">`;
    document.getElementById("ccdropdown").innerHTML =
    `<a class="dropdown-item active" href="javascript:void(0);" onclick="hidecc()">Cc</a>`;
}

function hidecc(){
    document.getElementById("cc").innerHTML = "";
    document.getElementById("ccdropdown").innerHTML =
    `<a class="dropdown-item" href="javascript:void(0);" onclick="displaycc()">Cc</a>`;
}

function displaybcc(){
    document.getElementById("bcc").innerHTML = 
    `<h4>Bcc: </h4>
    <input type="text" class="form-control bg-transparent" placeholder=" Bcc:">`;
    document.getElementById("bccdropdown").innerHTML =
    `<a class="dropdown-item active" href="javascript:void(0);" onclick="hidebcc()">Bcc</a>`;
}

function hidebcc(){
    document.getElementById("bcc").innerHTML = "";
    document.getElementById("bccdropdown").innerHTML =
    `<a class="dropdown-item" href="javascript:void(0);" onclick="displaybcc()">Bcc</a>`;
}

function displayreplyto(){
    document.getElementById("replyto").innerHTML = 
    `<h4>Reply To: </h4>
    <input type="text" class="form-control bg-transparent" placeholder=" Reply to:">`;
    document.getElementById("replytodropdown").innerHTML =
    `<a class="dropdown-item active" href="javascript:void(0);" onclick="hidereplyto()">Reply to</a>`;
}

function hidereplyto(){
    document.getElementById("replyto").innerHTML = "";
    document.getElementById("replytodropdown").innerHTML =
    `<a class="dropdown-item" href="javascript:void(0);" onclick="displayreplyto()">Reply to</a>`;
}

async function validateemailcredentials(){
    const form = document.getElementById('createalias');
    const item = {
        "sendername": form.sendername.value.trim(),
        "senderemail": form.senderemail.value.trim(),
        "newaliasemail":  form.newaliasemail.value.trim() !== "" ? form.newaliasemail.value.trim() : form.senderemail.value.trim(),
        "newemailpassword": form.newemailpassword.value.trim(),
        "createdon": new Date().toISOString().replace('T', ' ').replace(/\..+/, '')
    };

    try {
        const response = await fetch('createalias', {
            method: 'POST',
            body: JSON.stringify(item),
            headers: {
                'X-CSRFToken': getCookie('csrftoken')  // Add CSRF token for Django
            }
        });

        if (response.ok) {
            const data = await response.json();
            if(data["success"]){
                document.getElementById("isverified").innerHTML =
                `<div class="alert alert-success" role="alert">
                    <strong>${data["message"]}</strong>
                 </div>`;
                 var aliastable = ""
                 for (const key of Object.keys(data["items"])) {
                    aliastable += `<tr>
                    <td data-label="Name">${data["items"][key]["sendername"]}</td>
                    <td data-label="Sender">${data["items"][key]["newaliasemail"]}</td>
                    <td data-label="Useremail">${data["items"][key]["senderemail"]}</td>
                    <td data-label="Verified on">${data["items"][key]["createdon"]}</td>
                    <td data-label="Status">Select</td>
                    </tr>`
                  }
                  document.getElementById("verifiedemailslist").innerHTML = aliastable;
            }else{
                document.getElementById("isverified").innerHTML =
                `<div class="alert alert-danger" role="alert">
                    <strong>${data["message"]}</strong>
                 </div>`;
            }
        } else {
            const errorData = await response.json();
            console.log(errorData)
        }
    } catch (error) {
        console.error('Error:', error);
    }
}