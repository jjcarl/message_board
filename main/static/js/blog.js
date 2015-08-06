
function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}

$('#pin-btn').click(function(e){
    e.preventDefault();
    var id = $(this).parent().attr('data-post-id');
    $.ajax({
        url: '/message/message-detail/' + id +'/',
        method: 'PUT',
        data: {
            'type': 'pin'
        },
        beforeSend: function(xhr){
                xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"))
            },
        success: function() {
                $('#message-id-row').append('<p><center>You have changed your pin preference for this message</center></p>');
            }
    })
})


$('#favorite-btn').click(function(e){
    e.preventDefault();
     var id = $(this).parents($('#favorite-field')).attr('data-post-id');
    $.ajax({
        url: '/message/message-detail/' + id +'/',
        method: 'POST',
        data: {
            'type': 'favorite',
        },
        beforeSend: function(xhr){
                xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"))
            },
        success: function() {
                $('#message-id-row').append('<p><center>You favorited this message</center></p>');
            }
    })
})

$('#unfavorite-btn').click(function(e){
    e.preventDefault();
     var id = $(this).parent().attr('data-post-id');
    $.ajax({
        url: '/message/message-detail/' + id +'/',
        method: 'POST',
        data: {
            'type': 'unfavorite',
        },
        beforeSend: function(xhr){
                xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"))
            },
        success: function() {
                $('#message-id-row').append('<p><center>You have un-favorited this message</center></p>');
            }
    })
})


$('.all-messages').on('click', '.one-message', function(e){
    e.preventDefault();
    var message = $(this).parents('.row').attr('data-post-id');
    if (confirm('Are you sure you want to delete this message?')){
        
        $.ajax({
            url: '/message/message-detail/' + message + '/',
            method: 'DELETE',
            beforeSend: function(xhr){
                xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"))
            },
            success: function(){
                $('div[data-post-id=' + message + ']').remove();
            }
        })
    }
    
});

$('#delete-message').click(function(e){
    e.preventDefault();
    var message = $(this).parent().attr('data-post-id');
    if (confirm('Are you sure you want to delete this message?')){
        
        $.ajax({
            url: '/message/message-detail/' + message + '/',
            method: 'DELETE',
            beforeSend: function(xhr){
                xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"))
            },
        })
    }
    
});

$('#create-message-comment').click(function(e){
    e.preventDefault();
    $('#comment-form').show();
});

// $('#submit-message-comment').click(function(e){
//     e.preventDefault();
//     $('#comment-form').hide();
// });