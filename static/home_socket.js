$(document).ready(function() {

    var socket = io.connect("https://livealifekok.appspot.com");
    //var socket = io.connect("http://localhost:8080");

    socket.on("connect", function() {
        console.log("User is connecting ...");
    });

    socket.on("message", function(msg) {
        $("#messages").append("<li>"+msg+"</li>");
        console.log("Received message: " + msg);
    });

    $("#send").on('click', function() {
        socket.send($("#myMsg").val());
        $("#myMsg").val('');
    });
});
