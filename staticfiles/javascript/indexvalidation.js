console.log("signin hey");
$(document).ready(function ($) {
  $("#loginformuser").validate({
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
      email: "Please enter your email",
    },
  });
  $("#second_form").validate({
    rules: {
      name: "required",
      password: {
        required: true,
        minlength: 6,
      },
      profile: "required",
      email: "required",
      number: "required",
      gender: "required",
    },
    messages: {
      name: "Please enter your Name",
      password: {
        required: "Please provide a password",
        minlength: "Your password must be at least 6 characters long",
      },
      email: "Please enter your email",
      number: "Please enter your number",
      gender: "This field is required",
    },
    errorPlacement: function (error, element) {
      if (element.is(":radio")) {
        error.appendTo(element.parents(".form-group"));
      } else {
        error.insertAfter(element);
      }
    },
    submitHandler: function (form) {
      form.submit();
    },
  });
});
