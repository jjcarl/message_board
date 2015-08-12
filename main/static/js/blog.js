// ===== Show Navbar when scrolling up ======
jQuery(document).ready(function($) {
    var MQL = 1170;

    //primary navigation slide-in effect
    if ($(window).width() > MQL) {
        var headerHeight = $('.navbar-custom').height();
        $(window).on('scroll', {
                previousTop: 0
            },
            function() {
                var currentTop = $(window).scrollTop();
                //check if user is scrolling up
                if (currentTop < this.previousTop) {
                    //if scrolling up...
                    if (currentTop > 0 && $('.navbar-custom').hasClass('is-fixed')) {
                        $('.navbar-custom').addClass('is-visible');
                    } else {
                        $('.navbar-custom').removeClass('is-visible is-fixed');
                    }
                } else {
                    //if scrolling down...
                    $('.navbar-custom').removeClass('is-visible');
                    if (currentTop > headerHeight && !$('.navbar-custom').hasClass('is-fixed')) $('.navbar-custom').addClass('is-fixed');
                }
                this.previousTop = currentTop;
            });
    }
});


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
            success: function(){
                window.location.href = '/message/message-board/';
            }
        })
    }
    
});

$('#create-message-comment').click(function(e){
    e.preventDefault();
    $('#comment-form').show();
});

// ============== Edit Message ===========

$('#edit-message-btn').click(function(e){
    e.preventDefault();
    $('#edit-message-form').show();
    var id = $(this).parent().attr('data-post-id');

    $.get('/message/message-detail/' + id + '/json/', function(data){

        var text = data[0].fields.text
        var title = data[0].fields.title
        var id = data[0].pk
        var author = data[0].fields.author
        var media = data[0].fields.media
        var post_type = data[0].fields.post_type

        $('#edit-message-form input[name="author"]').val(author);
        $('#edit-message-form input[name="title"]').val(title);
        $('#edit-message-form textarea[name="text"]').val(text);
        $('#edit-message-form input[name="id"]').val(id);
        if (media.length > 0){
            $('#edit-message-form select[name="post_type"]').val(post_type);
        }
    });
})

$('#cancel-button').click(function(e){
    e.preventDefault();
    clearForm();
});

function clearForm(){
    $('#edit-message-form input[name="author"]').val('');
    $('#edit-message-form input[name="title"]').val('');
    $('#edit-message-form textarea[name="text"]').val('');
    $('#edit-message-form input[name="id"]').val('');
    $('#edit-message-form input[name="media"]').val('');
    $('#edit-message-form').hide();
}


$('#create-message-form select[name="post_type"]').change(function(){
    switch ($(this).val()){
        case 'QTE':
            $('#quote-reference').show();
            $('#media-link').hide();
            break;
        case 'VID':
            $('#media-link').show();
            $('#quote-reference').hide();
            break;
        case 'AUD':
            $('#media-link').show();
            $('#quote-reference').hide();
            break;
        case 'PST':
            $('#media-link').hide();
            $('#quote-reference').hide();
            break;
    }
});

$('#create-message-form select[name="post_type"]').change(function(){
    switch ($(this).val()){
        case 'QTE':
            $('#edit-quote-reference').show();
            $('#edit-media-link').hide();
            break;
        case 'VID':
            $('#edit-media-link').show();
            $('#edit-quote-reference').hide();
            break;
        case 'AUD':
            $('#edit-media-link').show();
            $('#edit-quote-reference').hide();
            break;
        case 'PST':
            $('#edit-media-link').hide();
            $('#edit-quote-reference').hide();
            break;
    }
});


