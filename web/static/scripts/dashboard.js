$(document).ready(() => {
    $('.nav-el').hover(function() {
        $(this).find('#nav-icon-cont').addClass('nav-icon-cont');
    }, function() {
        $(this).find('#nav-icon-cont').removeClass('nav-icon-cont');
    });
})
