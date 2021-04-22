$('#send_message').submit(function(e){
    e.preventDefault()
    var action=$(this).attr('action')
    $.ajax({
        url: action,
        method: 'POST',
        data:$(this).serialize(),
        success:function(response){
            console.log(response);
            $('#messages').html(response)
        }
    })
})