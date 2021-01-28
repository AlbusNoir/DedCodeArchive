'''
    Abstract base class for tree
'''
class Tree:
    '''abstract class for representing tree'''

    #--------------nested position class---------
    class Position:
        '''abstract representing location of element
        '''

        def element(self):
            '''return element stored at this position'''
            raise NotImplementedError('Must be implemented by subclass')

        def __eq__(self, other):
            '''True if other pos is same'''
            raise NotImplementedError('Must be implemented by subclass')

        def __ne__(self, other):
            '''True is other NOT same'''
            return not (self == other)  # op of __eq__


    #----------abstract methods to create subclass----------------------------
    def root(self):
        '''return pos for tree root'''
        raise NotImplementedError('Must be implemented by subclass')

    def parent(self, p):
        '''return pos of p's parent'''
        raise NotImplementedError('Must be implemented by subclass')

    def num_children(self, p):
        '''return num children of p'''
        raise NotImplementedError('Must be implemented by subclass')

    def children(self, p):
        '''iteration of positions representing p's children'''
        raise NotImplementedError('Must be implemented by subclass')

    def __len__(self):
        '''return total num of elements'''
        raise NotImplementedError('Must be implemented by subclass')

    #--------concrete methods-------------
    def is_root(self, p):
        '''True if pos is root'''
        return self.root() == p

    def is_leaf(self, p):
        '''True is pos p does not have children'''
        return self.num_children(p) == 0

    def is_empty(self):
        '''True if tree is empty'''
        return len(self) == 0


    #---------depth and height-----------
    def depth(self, p):
        '''return num levels separating p from root'''
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height1(self, p):
        '''return height of tree'''
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def height2(self, p):
        '''return height of subtree rooted at p'''
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        '''return height of subtree at p.
        If p is None, return height of entire tree'''
        if p is None:
            p = self.root()
        return self._height2(p)  # recur height2
