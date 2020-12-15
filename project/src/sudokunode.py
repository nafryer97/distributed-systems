from wirepickle.server import expose, Server

class NodePeer:
    ''' is composed of a server and client; is a peer in the system '''
    def __init__(self,peers,pos=0):
        ''' '''
        self.peers = peers
        

    def get_neighbors(self,peers,pos=0):
        ''' '''
        pass

class NodeClient:
    ''' asks other nodes to do things '''

    def __init__(self,neighbors,square,grid,pos=0):
        ''' '''
        self.neighbors=neighbors
        self.square=square
        self.grid=grid
        self.pos=pos

class NodeServer:
    ''' does things for other nodes '''

    def __init__(self,square,grid,pos=0):
        ''' '''
        self.square=square
        self.grid=grid
        self.pos=pos

    @expose('solve')
    def solve(self, caller_pos, row=0):
        ''' '''
        pass

    @expose('get_pos')
    def get_pos(self, caller_pos):
        ''' '''
        pass

    @expose('get_square')
    def get_square(self, caller_pos):
        ''' '''
        pass

    @expose('get_row')
    def get_row(self, caller_pos, r):
        ''' '''
        pass

    @expose('get_col')
    def get_col(self,caller_pos, c):
        ''' '''
        pass

    @expose('get_neighbor_square')
    def get_neighbor_square(self, caller_pos, neighbor_pos):
        ''' '''
        pass

    @expose('get_neighbor_row')
    def get_neighbor_row(self,caller_pos,neighbor_pos,r):
        ''' '''
        pass

    @expose('get_neighbor_col')
    def get_neighbor_col(self,caller_pos,neighbor_pos,c):
        ''' '''
        pass

    @expose('update_square')
    def update_square(self, caller_pos, sqaure):
        ''' '''
        pass

    @expose('update_row')
    def update_row(self, caller_pos,r,row):
        ''' '''
        pass

    @expose('update_col')
    def update_col(self, caller_pos,c,col):
        ''' '''
        pass