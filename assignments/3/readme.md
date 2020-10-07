# Assignment 3

## Encryption Scheme

In the encryption message I attempted to implement a simple RSA encryption scheme using an example on [wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)). It didn't turn out exactly correctly, but it's late, close to the deadline, and I'm mostly just happy that I figured the gRPC out. I use an integer n = pq, an exponent e that is coprime with (p-1)(q-1), and an integer d that is the modular multiplicative inverse of e. The encrypted message is an integer m. The public key is n, e and the private key is n, d. The client requests the public key from the server, and uses that public key to encrypt m. Then the client sends the encrypted m to the server, which proceeds to decrypt it and then print it. 

## Gif

In the gif I run <code> docker-compose up --build </code> and then docker initiates the two clients and the server. The clients say hello to the server, they exchange keys, and then the server prints out the messages that it received from the clients.


