$(document).ready(() => {
    $('#register').hover(() => {
        const registerType = $('#register-type');
            registerType.css("display", "flex")
            registerType.animate({left: "10em"}, 200)
            registerType.addClass('register-type-hovered')
        }, () => {
            $('#register-type').animate({left: -0}, 100)
            $('#register-type').css("display", "none")
        }
    )
    $('#register-type').hover(() => {
        $(this).addClass('register-type-hovered')
    }, () => {
        $(this).removeClass('register-type-hovered')
    }
    )
});
