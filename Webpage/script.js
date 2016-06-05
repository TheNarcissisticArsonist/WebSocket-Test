var ws = new WebSocket("ws://127.0.0.1:12345/");
ws.onmessage = function (event) {
    var message = event.data;
    document.body.innerHTML = message + "<br>" + document.body.innerHTML;
};