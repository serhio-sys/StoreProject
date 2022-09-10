$(".stars-form").submit(function(e){
    e.preventDefault();
    var action_url = $(this).attr("action")
    formData = new FormData($(this).get(0));
    $.ajax({
        type: "GET",
        url: action_url,
        data: formData,
        contentType: false,
        processData: false,
        success: function(response){
            if ("part" in response){
                document.querySelector('.stars').innerHTML = response['part']
            }
            else{
                window.location.reload()
            }
        }
    })
})