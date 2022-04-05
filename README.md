# P2P-Chat-App
This is the P2P chat app for Joe and Justin. Built for the EC530 hackathon.

There are two folders, the `ChatApp/` was a failed attempt at building a P2P
app using react-native and expo. It turns out that there are not many
cross-platform socket libraries that work well across web, android, and iOS
and we had trouble using this setup on the BU network.

As an alternative, we developed a simple TCP based system where there is a
server and a client, and clients cna broadcast messages to each other via the
server. As demoed in class, the server was running on a remote virtual machine
with a public IP address that clients could connect to. The server was quite
dumb in that it accepted connections from any client and broadcast any message
sent to it to all connected clients. While simple, this basic architecture
allowed us to send messages back and forth, even when on separate networks. The
server was not storing or logging any of the traffic, and it was up to the
clients to take care to send messages such that only intended audiences can
render them.

On top of this scheme, we added a simple example of having the clients
encrypt and send messages through the server using a symmetric key. For demo
purposes the key has to be provided when starting the client, but it showed
the proof of concept that the client could be responsible for sending
and receiving messages to one another, taking care of their own encryption.

The server basically just played the role of being a relay. It could be
developed into a more sophisticated router or discovery server, allowing
clients to share information using public keys or other cryptographic
mechanisms without needing to store or provide any actual chat features to
connected clients.

The server is in `python/server.py` and the client in `python/client.py`.

