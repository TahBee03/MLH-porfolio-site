// SOURCE: https://www.w3schools.com/howto/howto_js_shrink_header_scroll.asp
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
        document.getElementById("nav-bar").style.height = "115px";
        document.getElementById("nav-logo").style.transform = "translate(" + -650 + "px," + 0 + "px) scale(" + 0.75 + ")";
        document.getElementById("profile-picture").style.transform = "translate(" + 0 + "px," + -150 + "px) scale(" + 0.30 + ")";
        document.getElementById("title").style.transform = "translate(" + 0 + "px," + -250 + "px) scale(" + 0.5 + ")";
        document.getElementById("tabs").style.transform = "translate(" + 525 + "px," + -340 + "px) scale(" + 1 + ")";
        document.getElementById("main").style.transform = "translate(" + 0 + "px," + -5 + "px)";
    } else {
        document.getElementById("nav-bar").style.height = "425px";
        document.getElementById("nav-logo").style.transform = "translate(" + 0 + "px," + 0 + "px) scale(" + 1 + ")";
        document.getElementById("profile-picture").style.transform = "translate(" + 0 + "px," + 0 + "px) scale(" + 1 + ")";
        document.getElementById("title").style.transform = "translate(" + 0 + "px," + 0 + "px) scale(" + 1 + ")";
        document.getElementById("tabs").style.transform = "translate(" + 0 + "px," + 0 + "px) scale(" + 1 + ")";
        document.getElementById("main").style.transform = "translate(" + 0 + "px," + 0 + "px)";
    }
}