$(document).ready(function(){
    $(document).on('click', '.historyAPI', function(e){
        e.preventDefault();
        var href = $(this).attr('href');
        console.log(href);
        // Getting Content
        getContent(href, true);

        $('.historyAPI').parent().removeClass('active');
        $(this).parent().addClass('active');
    });
});

// Adding popstate event listener to handle browser back button
window.addEventListener("popstate", function(e) {
    // Get State value using e.state
    getContent(location.pathname, false);
});

function getContent(url, addEntry) {
    $.get(url)
    .done(function( data ) {
        // Updating Content on Page
        $('.content-page').html($(data).find(".content-page").html());

        if(addEntry == true) {
            // Add History Entry using pushState
            history.pushState(null, null, url);
        }

    });
}