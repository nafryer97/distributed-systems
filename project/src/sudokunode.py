"""
    Module for individual nodes in system; provides server and client functionality
    because members are peers

"""

from wirepickle.server import expose, Server
from wirepickle.client import Client
from sudokuboard import Grid, Square
import time 

class NodePeer:
    ''' is composed of a server and client; is a peer in the overall system '''
    def __init__(self,neighbors,pos):
        ''' '''
        self.pos = pos
        self.grid = Grid()
        self.peerinfo = DistributedPeerInfo()
        
        self.client = NodeClient(neighbors,self.grid,self.pos)
        self.server = NodeServer(self.grid,self.pos)

        Server(self.server).listen(self.peerinfo.address_from_position(self.pos))
        
        #self.client.broadcast_hello()

    def solve(self):
        ''' '''
        pass


class NodeClient:
    ''' asks other nodes to do things '''

    def __init__(self,neighbors,grid,pos):
        ''' '''
        self.neighbors=neighbors
        self.grid=grid
        self.pos=pos
        self.peerinfo = DistributedPeerInfo()

        if pos == 0:
            self.server1 = Client(self.peerinfo.address_from_position(1))
            self.server3 = Client(self.peerinfo.address_from_position(3))
        elif pos == 1:
            self.server0 = Client("tcp://127.0.0.1:57301")
            self.server2 = Client(self.peerinfo.address_from_position(2))
        elif pos == 2:
            self.server1 = Client(self.peerinfo.address_from_position(1))
            self.server4 = Client(self.peerinfo.address_from_position(4))
            self.server5 = Client(self.peerinfo.address_from_position(5))
        elif pos == 3:
            self.server0 = Client("tcp://127.0.0.1:57301")
            self.server4 = Client(self.peerinfo.address_from_position(4))
            self.server6 = Client(self.peerinfo.address_from_position(6))
        elif pos == 4:
            self.server1 = Client(self.peerinfo.address_from_position(1))
            self.server3 = Client(self.peerinfo.address_from_position(3))
            self.server5 = Client(self.peerinfo.address_from_position(5))
            self.server7 = Client(self.peerinfo.address_from_position(7))
        elif pos == 5:
            self.server2 = Client(self.peerinfo.address_from_position(2))
            self.server4 = Client(self.peerinfo.address_from_position(4))
            self.server8 = Client(self.peerinfo.address_from_position(8))
        elif pos == 6:
            self.server3 = Client(self.peerinfo.address_from_position(3))
            self.server7 = Client(self.peerinfo.address_from_position(7))
        elif pos == 7:
            self.server4 = Client(self.peerinfo.address_from_position(4))
            self.server6 = Client(self.peerinfo.address_from_position(6))
        elif pos == 8:
            self.server5 = Client(self.peerinfo.address_from_position(5))
            self.server7 = Client(self.peerinfo.address_from_position(7))
            self.server8 = Client(self.peerinfo.address_from_position(8))
        else:
            print("I have a strange position number")

    def get_neighbor_square(self, neighbor_pos):
        ''' '''
        #if neighbor_pos in self.neighbors:
         #   return self.servers[neighbor_pos].get_square(self.pos)
        pass
    
    def get_neighbor_row(self, neighbor_pos, r):
        ''' '''
        #if neighbor_pos in self.neighbors:
         #   return self.servers[neighbor_pos].get_row(self.pos, r)
        pass
    
    def get_neighbor_col(self, neighbor_pos, c):
        ''' '''
        #if neighbor_pos in self.neighbors:
         #   return self.servers[neighbor_pos].get_col(self.pos, c)
        pass
    
    def get_neighbor_grid(self, neighbor_pos):
        ''' '''
        #if neighbor_pos in self.neighbors:
         #   return self.servers[neighbor_pos].get_grid(self.pos)
        pass
    
    def send_row(self, neighbor_pos, r):
        ''' '''
        #if neighbor_pos in self.neighbors:
         #   self.servers[neighbor_pos].update_row(self.pos,r,self.grid.get_square().get_row(r))
        pass
    
    def send_col(self, neighbor_pos, c):
        ''' this will have issues because it can't update the original on the receiver '''
        #if neighbor_pos in self.neighbors:
         #   self.servers[neighbor_pos].update_col(self.pos,c,self.grid.get_square().get_col(c))
        pass
    
    def send_square(self, neighbor_pos):
        ''' '''
        #if neighbor_pos in self.neighbors:
         #   self.servers[neighbor_pos].update_square(self.pos, self.grid.get_square())
        pass
    
    def send_grid(self, neighbor_pos):
        ''' '''
        pass

    def send_message(self, neighbor_pos):
        ''' sends a string to the server '''
        message = "hello from node " + str(self.pos) + "!"
        #if neighbor_pos in self.neighbors:
         #   self.servers[neighbor_pos].receive_message(self.pos,message)
        pass
    
    def broadcast_hello(self):
        ''' sends a hello message to all neighbors '''
        for i in self.neighbors:
            self.send_message(i)

class NodeServer:
    ''' does things for other nodes '''

    def __init__(self,grid,pos):
        ''' '''
        self.peerinfo = DistributedPeerInfo()
        self.grid=grid
        self.pos=pos

    @expose('solve')
    def solve(self, caller_pos, row=0):
        ''' '''
        pass

    @expose('get_pos')
    def get_pos(self, caller_pos):
        ''' returns the position of this node to the caller '''
        if self.check_position(caller_pos):
            return self.pos

    @expose('get_grid')
    def get_grid(self, caller_pos):
        ''' returns the entire sudoku board as this node knows it '''
        if self.check_position(caller_pos):
            return self.grid.get_grid()

    @expose('get_square')
    def get_square(self, caller_pos):
        ''' returns this node's square in the grid to the caller '''
        if self.check_position(caller_pos):
            return self.grid.get_square(self.pos)

    @expose('get_row')
    def get_row(self, caller_pos, r):
        ''' returns the specified row from this node's square to the caller '''
        if self.check_position(caller_pos):
            return self.grid.get_square(self.pos).get_row(r)

    @expose('get_col')
    def get_col(self,caller_pos, c):
        ''' returns the specified col from this node's square to the caller '''
        if self.check_position(caller_pos):
             return self.grid.get_square(self.pos).get_col(c)

    @expose('update_grid')
    def update_grid(self, caller_pos):
        ''' '''
        pass

    @expose('update_square')
    def update_square(self, caller_pos, square):
        ''' '''
        if self.check_position(caller_pos):
             for i in range(3):
                 for j in range(3):
                     self.grid.get_square(self.pos).assign_val(i,j,square[i][j])

    @expose('update_row')
    def update_row(self, caller_pos,r,row):
        ''' '''
        if self.check_position(caller_pos):
            for i in range(3):
                self.grid.get_square(self.get_pos).assign_val(r,i,row[i])

    @expose('update_col')
    def update_col(self, caller_pos,c,col):
        ''' '''
        pass

    @expose('good_choice_row')
    def good_choice_row(self, caller_pos,r,n):
        ''' ''' 
        if self.check_position(caller_pos):
             return self.grid.get_square(self.pos).check_num_row(r,n)

    @expose('good_choice_col')
    def good_choice_col(self, caller_pos,c,n):
        ''' '''
        if self.check_position(caller_pos):
            return self.grid.get_square(self.pos).check_num_col(c,n)

    def check_position(self, caller_pos):
        ''' checks to make sure the RPC is being called by an adjacent neighbor '''
        neighbors = self.peerinfo.adjacent_nodes(self.pos)
        return caller_pos in neighbors

    @expose('receive_message')
    def receive_message(self, caller_pos, message):
        if self.check_position(caller_pos):
            print(str(self.pos) + " received message: " + message + " from " + str(caller_pos))
            return 0
        return -1

    #@expose('get_neighbor_square')
    #def get_neighbor_square(self, caller_pos, neighbor_pos):
    #    ''' '''
    #    pass

    #@expose('get_neighbor_row')
    #def get_neighbor_row(self,caller_pos,neighbor_pos,r):
    #    ''' '''
    #    pass

    #@expose('get_neighbor_col')
    #def get_neighbor_col(self,caller_pos,neighbor_pos,c):
    #    ''' '''
    #    pass

class DistributedPeerInfo:
    ''' '''

    def position_from_hostname(self, name):
        ''' '''
        node_dict = { 
                "node0":0,
                "node1":1,
                "node2":2,
                "node3":3,
                "node4":4,
                "node5":5,
                "node6":6,
                "node7":7,
                "node8":8
            }

        return node_dict.get(name,-1)

    def address_from_position(self,pos):
        ''' '''
        address_dict = {
                0:"tcp://127.0.0.1:57301",
                1:"tcp://127.0.0.1:57302",
                2:"tcp://127.0.0.1:57303",
                3:"tcp://127.0.0.1:57304",
                4:"tcp://127.0.0.1:57305",
                5:"tcp://127.0.0.1:57306",
                6:"tcp://127.0.0.1:57307",
                7:"tcp://127.0.0.1:57308",
                8:"tcp://127.0.0.1:57309"
            }

        return address_dict.get(pos,"")

    def position_from_address(self, address):
        ''' '''
        position_dict = {
            "tcp://127.0.0.1:57301":0,
            "tcp://127.0.0.1:57302":1,
            "tcp://127.0.0.1:57303":2,
            "tcp://127.0.0.1:57304":3,
            "tcp://127.0.0.1:57305":4,
            "tcp://127.0.0.1:57306":5,
            "tcp://127.0.0.1:57307":6,
            "tcp://127.0.0.1:57308":7,
            "tcp://127.0.0.1:57309":8
            }

        return position_dict.get(address,-1)

    def port_from_position(self,pos):
        ''' '''
        port_dict = {
            0:"tcp://*:57301",
            1:"tcp://*:57302",
            2:"tcp://*:57303",
            3:"tcp://*:57304",
            4:"tcp://*:57305",
            5:"tcp://*:57306",
            6:"tcp://*:57307",
            7:"tcp://*:57308",
            8:"tcp://*:57309",
        }
        return port_dict.get(pos, -1)

    def adjacent_nodes(self,pos):
        ''' '''
        adjacency_dict = {
            0:[1,3], 
            1:[0,2,4], 
            2:[1,5], 
            3:[0,4,6],
            4:[1,3,5,7], 
            5:[2,4,8], 
            6:[3,7], 
            7:[4,6,8], 
            8:[7,5]
            }

        return adjacency_dict.get(pos,[])