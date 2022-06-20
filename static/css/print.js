$("#btn").click(function () {
    //Hide all other elements other than printarea.
    $("#DivIdToPrint").show();
    $("body").css({"margin": "0px"});
    $("body").css({"margin-left": "50px"});
    $("body").css({"width": "650px"});
    $("#Hide").hide();
    window.print();
});