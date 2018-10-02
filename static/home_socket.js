$(document).ready(function() {

    var socket = io.connect("http://localhost:8080");

    socket.on("connect", function() {
        socket.send("User has connected!");
    });

    socket.on("message", function(msg) {
        console.log("Received message: " + msg);
    });

});
