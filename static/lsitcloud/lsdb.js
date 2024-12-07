document.getElementById('submitCreateTable').addEventListener('click', function () {
    const form = document.getElementById('createTableForm');
    const tableName = form.table_name.value.trim();
    const primaryKey = form.primary_key.value.trim();
    const keyType = form.key_type.value;

    // Validate form inputs
    if (tableName.length < 3 || tableName.length > 255) {
        alert("Table name must be between 3 and 255 characters.");
        return;
    }
    if (primaryKey.length < 1 || primaryKey.length > 255) {
        alert("Primary key must be between 1 and 255 characters.");
        return;
    }

    // Make an AJAX request to the server
    fetch('createtable', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Include CSRF token for security
        },
        body: JSON.stringify({
            table_name: tableName,
            primary_key: primaryKey,
            key_type: keyType
        })
    }).then(response => response.json()).then(data => {
            if (data.success) {
                alert(`Table '${tableName}' created successfully!`);
                // Optionally, close the modal
                const modal = document.getElementById('modaldemo1');
                const modalInstance = bootstrap.Modal.getInstance(modal);
                modalInstance.hide();
            } else {
                alert(`Error: ${data.error}`);
            }
        }).catch(error => {
            console.error('Error:', error);
            alert('An error occurred while creating the table.');
        });
});

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