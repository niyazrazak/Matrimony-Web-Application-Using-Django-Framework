$.ajaxSetup({
    headers: {
        'X-CSRFToken': '{{csrf_token}}'
    }
});


function deleteStaff(id) {
    console.log("hai Monu");
    $.ajax({
        type: "POST",
        url: "/deletestaff/",
        data: {
            id: id
        },
        success: function(response) {
            alert(response.msg)
        }
    });
}