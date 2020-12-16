from sudokunode import NodePeer, DistributedPeerInfo
from concurrent import futures
import socket
import logging

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(name)s %(message)s', level=logging.DEBUG)

    peerinfo = DistributedPeerInfo()

    pos = peerinfo.position_from_hostname(socket.gethostname())
    neighbors = peerinfo.adjacent_nodes(pos)
    addresses = [peerinfo.address_from_position(i) for i in neighbors]

    node = NodePeer(neighbors,pos)

    print("Done")
