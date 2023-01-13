// $(document).ready(function () {
//   $(".side-nav-group").click(function () {
//     $(this).addClass("active").siblings().removeClass("active");
//   });
// });
$(document).ready(function () {
    $("nav div a").click(function () {
        $("nav div .side-nav-group").removeClass("active");
        $(this).addClass("active");
    });

    var current_path = window.location
    $("nav div .side-nav-group").removeClass("active");
    $.each($("nav .side-nav-group"), function( key, value ) {
        if (window.location.href == value){
            $(this).addClass("active");
        }
    });
    
});