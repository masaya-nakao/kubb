document.addEventListener('DOMContentLoaded', function () {
    var chatMessages = document.getElementById('chat-messages');
    var usernameInput = document.getElementById('username');
    var messageInput = document.getElementById('message');
    var sendButton = document.getElementById('send-button');

    sendButton.addEventListener('click', function () {
        var username = usernameInput.value;
        var message = messageInput.value;

        if (username && message) {
            sendMessage(username, message);
            messageInput.value = '';
        }
    });

    function sendMessage(username, message) {
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '', true);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                // メッセージ送信成功時の処理
            }
        };

        var data = 'username=' + encodeURIComponent(username) + '&message=' + encodeURIComponent(message);
        xhr.send(data);
    }
});
