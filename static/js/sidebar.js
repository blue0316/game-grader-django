// $(document).ready(function () {
//   $(".side-nav-group").click(function () {
//     $(this).addClass("active").siblings().removeClass("active");
//   });
// });
$(document).ready(function () {
    $("aside div a").click(function () {
        $("aside div .side-nav-group").removeClass("active");
        $(this).addClass("active");
        console.log("hello");
    });

    var current_path = window.location
    $("aside div .side-nav-group").removeClass("active");
    $.each($("aside .side-nav-group"), function( key, value ) {
        if (window.location.href == value){
            $(this).addClass("active");
        }
    });
    
});
function toggleSidebar() {
    const aside = document.querySelector('aside')
    aside.classList.toggle("sm:hidden")
    aside.classList.toggle("hidden")
}