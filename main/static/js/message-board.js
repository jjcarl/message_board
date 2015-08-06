var page = 0;
var date = Date();
loadMessages(page);

function loadMessages(page) {
    $.ajax({
            url: '/message/short-messages/',
            data: {
                page:page
            },
            success: function(result){
                
                $('#message-list').append(result)
                page++
                
            }
        })
}

$(window).scroll(function() {
    if ($(window).scrollTop() === $(document).height() - $(window).height()) {
        $('#load-more-messages').show();
        page++;
        $.ajax({
            url: '/message/short-messages/',
            data: {
                page:page
            },
            success: function(result){
                if (result.length > 0){
                    $('#message-list').append(result);
                    $('#load-more-messages').hide();
                    
                } else{
                    $('#load-more-messages').html('<center><h3>** No more posts to show. **</h3></center>');
                }
            }
        });
    }
});

$('#refresh-content').on('click', function(){

    $.ajax({
        url: '/message/short-messages/',
        success: function(result){
            $('#message-list').html(result);
        }
    });
});
