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