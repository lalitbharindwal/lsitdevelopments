async function createTable() {
    // Get form data
    const form = document.getElementById('createTableForm');
    const tablename = form.tablename.value.trim();
    const primaryKey = form.primarykey.value.trim();
    const keyType = form.keytype.value;

    // Validate form inputs
    if (tablename.length < 3 || tablename.length > 255) {
        alert("Table name must be between 3 and 255 characters.");
        return;
    }
    if (primaryKey.length < 1 || primaryKey.length > 255) {
        alert("Primary key must be between 1 and 255 characters.");
        return;
    }

    // Make an AJAX request to the server
    await fetch('lsdbcreatetable', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Include CSRF token for security
        },
        body: JSON.stringify({
            tablename: tablename,
            primarykey: primaryKey,
            keytype: keyType
        })
    }).then(response => response.json()).then(data => {
        if (data.success) {
            // Optionally, close the modal
            const modal = document.getElementById('modaldemo1');
            const modalInstance = bootstrap.Modal.getInstance(modal);
            modalInstance.hide();
            alert(`Table '${tablename}' created successfully!`);
            location = "lsdbtables";
        } else {
            alert(`Error: ${data.error}`);
        }
    }).catch(error => {
        console.error('Error:', error);
        alert('An error occurred while creating the table.');
    });
}

function deletetable(tablename){
    fetch('lsdbdeletetable', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Include CSRF token for security
        },
        body: JSON.stringify({
            tablename: tablename
        })
    }).then(response => response.json()).then(data => {
        if (data.success) {
            alert(`Table '${tablename}' deleted successfully!`);
            location = "lsdbtables"
        } else {
            alert(`Error: ${data.error}`);
        }
    }).catch(error => {
        console.error('Error:', error);
        alert('An error occurred while creating the table.');
    });
}

function deleteattribute(tablename, key){
    fetch('lsdbdeleteattribute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Include CSRF token for security
        },
        body: JSON.stringify({
            tablename: tablename,
            primarykeyvalue: key
        })
    }).then(response => response.json()).then(data => {
        if (data.success) {
            alert(`Table '${key}' deleted successfully!`);
            location.reload();
        } else {
            alert(`Error: ${data.error}`);
        }
    }).catch(error => {
        alert('An error occurred while creating the table.');
    });
}

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