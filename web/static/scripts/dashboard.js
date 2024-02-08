$(document).ready(() => {
    $('#register').click(() => {
        window.location.href = 'http://localhost:5000/admin/register'
    });
    $('#dasboard > .side-nav').hover(() => {
        $(this).addClass('nav-icon-cont')
    });
});
