console.log("addstaff");
$(document).ready(function() {
    $("#addstaff").validate({
        rules: {
            name: "required",
            designation: "required",
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
            name: "Please enter the new staff name",
            designation: "Please enter the designation of the staff",
            password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 6 characters long",
            },
            email: "Please enter the staff name"
        },
    });
});