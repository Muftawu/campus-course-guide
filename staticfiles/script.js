$(document).ready(function() {
    function handleFormSubmit(form) {
        var formData = form.serialize(); 
        var messagesContainer = $('#' + form.attr('id') + '-messages'); 

        $.ajax({
            type: form.attr('method'),
            url: form.attr('action'),
            data: formData,
            success: function(response) {
                if (response.redirect) {
                    window.location.href = response.redirect;
                }
                if (response.message) {
                    messagesContainer.html('<div class="alert alert-success" role="alert">' + response.message + '</div>');
                }
            },
            error: function(xhr) {
                var errors = JSON.parse(xhr.responseText);
                if (errors.error) {
                    messagesContainer.html('<div class="alert alert-danger" role="alert">' + errors.error + '</div>');
                }
            }
        });
    }

    // Bind AJAX form submission handler to each form
    $('#login-form').on('submit', function(event) {
        event.preventDefault();
        handleFormSubmit($(this));
    });

    $('#register-form').on('submit', function(event) {
        event.preventDefault(); 
        handleFormSubmit($(this)); 
    });

    // $('#upload-book-slide-resource-form').on('submit', function(event) {
    //     event.preventDefault(); 
    //     handleFormSubmit($(this)); 
    // });

    // $('#upload-video-resource-form').on('submit', function(event) {
    //     event.preventDefault(); 
    //     handleFormSubmit($(this)); 
    // });
});



