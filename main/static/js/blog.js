// ===== Show Navbar when scrolling up ======
jQuery(document).ready(function($) {

    //primary navigation slide-in effect
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
});

// ========== CSRF cookie function =======
function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}

// ======== Pin a message to the front page ========

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


// =============== Favorite, unfavorite a message ==============

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


// =========== Delete a message ======

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

// ========= Search Function =========

// $('#search-form').on('click', '#search-btn', function(){
//     var word = $(this).parent().val();
//     $.ajax({
//         url: '/message/message-search/',
//         method: 'GET',
//         word: word,
//         beforeSend: function(xhr){
//                 xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"))
//             },
//             success: function(){
                
//             }
//     })
// })

// ======== Show the form to comment on a mesasge ======

$('#create-message-comment').click(function(e){
    e.preventDefault();
    $('#comment-form').show();
});

// ============== Edit Message functions ===========

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
        var link = data[0].fields.link
        var reference = data[0].fields.reference

        $('#edit-message-form input[name="author"]').val(author);
        $('#edit-message-form input[name="title"]').val(title);
        $('#edit-message-form textarea[name="text"]').val(text);
        $('#edit-message-form input[name="id"]').val(id);
        $('#edit-message-form select[name="post_type"]').val(post_type);
        $('#edit-message-form input[name="link"]').val(link);
        $('#edit-message-form input[name="reference"]').val(reference);
        switch ($('#edit-message-form select[name="post_type"]').val()){
            case 'QTE':
                $('#edit-quote-reference').show();
                $('#edit-media-link').hide();
                break;
            case 'YTB':
                $('#edit-media-link').show();
                $('#edit-quote-reference').hide();
                break;
            case 'VMO':
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
    $('#edit-message-form input[name="link"]').val('');
    $('#edit-message-form select[name="post_type"]').val('');
    $('#edit-message-form').hide();
}


$('#create-message-form select[name="message-post_type"]').change(function(){
    switch ($(this).val()){
        case 'QTE':
            $('#quote-reference').show();
            $('#media-link').hide();
            break;
        case 'YTB':
            $('#media-link').show();
            $('#quote-reference').hide();
            break;
        case 'VMO':
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

$('#edit-message-form select[name="message-post_type"]').change(function(){
    switch ($(this).val()){
        case 'QTE':
            $('#edit-quote-reference').show();
            $('#edit-media-link').hide();
            break;
        case 'YTB':
            $('#edit-media-link').show();
            $('#edit-quote-reference').hide();
            break;
        case 'VMO':
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

if (window.innerWidth > 700){
    $('.project-preview').on('click', '.current-project-preview-pic', function(){
        if ($(this).attr('size') === '100') {
            $(this).animate({width: '100%'})
            $(this).attr('size', '500')
        } else if ($(this).attr('size') === '500') {
            $(this).animate({width: '15em'})
            $(this).attr('size', '100')
        }
    })

    $('.project-preview').on('click', '.project-preview-pic', function(){
        if ($(this).attr('size') === '100') {
            $(this).animate({width: '100%'})
            $(this).attr('size', '500')
        } else if ($(this).attr('size') === '500') {
            $(this).animate({width: '12em'})
            $(this).attr('size', '100')
        }
    })
}
