$(document).ready(() => {
    $('.nav-el').hover(function() {
        $(this).find('#nav-icon-cont').addClass('nav-icon-cont');
    }, function() {
        $(this).find('#nav-icon-cont').removeClass('nav-icon-cont');
    });
    $('#nav-register').click(() => {
        window.location.href = 'http://localhost:5000/admin/register'
    });
    $('#nav-blog').click(() => {
        window.location.href = 'http://localhost:5000/admin/blog'
    });
})
