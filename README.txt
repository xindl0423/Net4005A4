# Assignment 4 NET4005

**Description**

Sending secure application messages between a Client and Server using hybrid encryption.

**Getting Started**

***Executing program***

To run the server file use:
    -python server.py will run the server section of the file
    - Sample format: 'python server.py'
    -The server will generate a 2048-bit RSA keys
    -It will then start listening for a client connection.

To run the client file use:
    -'python client.py'
    -The client will read the server's public key, generate a symmetric AES key, and send it securely to the server.
    -It will then prompt the user for messages to send in a secure chat session.
    -Type `quit` to end the chat.

## Contributors
Xindong Lin
