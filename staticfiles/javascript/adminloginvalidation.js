console.log("logHello");
$(document).ready(function() {
    $("#loginform").validate({
        rules: {
            password: {
                required: true,
                minlength: 6,
            },
            email: {
                required: true,
                email: true,
            },
        },
        messages: {
            password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 6 characters long",
            },
            email: "Please enter your email"
        },
    });
});