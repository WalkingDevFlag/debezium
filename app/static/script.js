var client_id = Date.now();
document.querySelector("#ws-id").textContent = client_id;
var ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);

ws.onmessage = function (event) {
  var messages = document.getElementById("messages");
  var messageData = event.data;
  var content = document.createTextNode(messageData);
  var message = document.createElement("li");

  if (messageData.includes("Updated")) {
    message.className = "create";
  } else if (messageData.includes("Deleted")) {
    message.className = "delete";
  }
  message.appendChild(content);
  messages.insertBefore(message, messages.firstChild);
};

function sendMessage(event) {
  var input = document.getElementById("messageText");
  if (input.value.trim() !== "") {
    ws.send(input.value);
    input.value = "";
  }
  event.preventDefault();
}
