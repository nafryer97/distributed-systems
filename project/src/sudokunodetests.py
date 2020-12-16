from distributedsudoku import DistributedPeerInfo
from sudokunode import NodePeer, NodeClient, NodeServer
import unittest

class TestDistributedPeerInfo(unittest.TestCase):
    ''' tests the return values from the dictionary methods '''
    def test_position_from_hostname(self):
        ''' tests to see if the dictionary is mapping hostnames to position integers '''
        peerinfo = DistributedPeerInfo()
        names = ("node0","node1","node2","node3","node4","node5","node6","node7","node8")
        vals = [0,1,2,3,4,5,6,7,8]
        positions = [peerinfo.position_from_hostname(i) for i in names]
        self.assertEqual(vals,positions)

    def test_address_from_position(self):
        ''' tests to see if dictionary is mapping addresses to positions '''
        peerinfo = DistributedPeerInfo()
        keys=(0,1,2,3,4,5,6,7,8)
        addresses=["tcp://127.0.0.1:57301","tcp://127.0.0.1:57302","tcp://127.0.0.1:57303","tcp://127.0.0.1:57304","tcp://127.0.0.1:57305","tcp://127.0.0.1:57306","tcp://127.0.0.1:57307","tcp://127.0.0.1:57308","tcp://127.0.0.1:57309"]

        entries = [peerinfo.address_from_position(i) for i in keys]

        self.assertEqual(addresses,entries)

    def test_position_from_address(self):
        ''' tests to see if dictionary is mapping positions to addresses '''
        peerinfo = DistributedPeerInfo()
        vals = [0,1,2,3,4,5,6,7,8]
        addresses=["tcp://127.0.0.1:57301","tcp://127.0.0.1:57302","tcp://127.0.0.1:57303","tcp://127.0.0.1:57304","tcp://127.0.0.1:57305","tcp://127.0.0.1:57306","tcp://127.0.0.1:57307","tcp://127.0.0.1:57308","tcp://127.0.0.1:57309"]

        entries = [peerinfo.position_from_address(i) for i in addresses]
        self.assertEqual(vals, entries)

    def test_adjacent_nodes(self):
        ''' tests to see if a list can be constructed from a dictionary value'''
        peerinfo = DistributedPeerInfo()
        pos = 4
        addresses = ["tcp://127.0.0.1:57302","tcp://127.0.0.1:57304","tcp://127.0.0.1:57306","tcp://127.0.0.1:57308"]
        
        neighbor_entries = peerinfo.adjacent_nodes(pos)
        address_entries = [peerinfo.address_from_position(i) for i in neighbor_entries]

        self.assertEqual(addresses,address_entries)

class TestPeer(unittest.TestCase):
    ''' tests NodePeer methods  '''
    pass

class TestClientGetNeighborData(unittest.TestCase):
    ''' tests NodeClient methods that request info from peers '''
    def test_get_neighbor_square(self):
        ''' '''
        pass

    def test_get_neighbor_row(self):
        ''' '''
        pass

    def test_get_neighbor_col(self):
        ''' '''
        pass

    def test_get_neighbor_grid(self):
        ''' '''
        pass

class TestClientSendData(unittest.TestCase):
    ''' tests NodeClient methods that send data to servers  '''
    def test_send_row(self):
        ''' '''
        pass

    def test_send_col(self):
        ''' '''
        pass

    def test_send_square(self):
        ''' '''
        pass

    def test_send_grid(self):
        ''' '''
        pass

class TestServerGetData(unittest.TestCase):
    ''' tests NodeServer methods that send data to clients '''
    def test_get_pos(self):
        ''' '''
        pass

    def test_get_square(self):
        ''' '''
        pass

    def test_get_row(self):
        ''' '''
        pass

    def test_get_col(self):
        ''' '''
        pass

class TestServerUpdate(unittest.TestCase):
    ''' tests the server update methods where clients send data to server '''
    def test_update_square(self):
        ''' '''
        pass

    def test_update_row(self):
        ''' '''
        pass

    
    def test_update_col(self):
        ''' '''
        pass

class TestServerUpdateNeighbor(unittest.TestCase):
    ''' tests server methods that add gossipping functionality  '''
    pass

if __name__ == '__main__':
    unittest.main()