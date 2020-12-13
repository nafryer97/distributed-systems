class Node:
    '''Represents a member of the system '''
    def __init__(self,position):
        self.position = position
        self.square = Square()

    def get_position(self):
        return self.position

