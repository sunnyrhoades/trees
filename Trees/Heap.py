'''
'''

from Trees.BinaryTree import BinaryTree, Node

class Heap(BinaryTree):
    '''
    FIXME:
    Heap is currently not a subclass of BinaryTree.
    You should make the necessary changes in the class declaration line above 
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the Heap.
        '''
        super().__init__()
        if xs:
            for x in xs:
                self.insert(x)

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command Heap([1,2,3])
        it's __repr__ will return "Heap([1,2,3])"

        For the Heap, type(self).__name__ will be the string "Heap",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of Heap will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__+'('+str(self.to_list('inorder'))+')'


    def is_heap_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether insert/delete functions
        are actually working.
        '''
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        The lecture videos have the exact code you need,
        except that their method is an instance method when it should have been a static method.
        '''
        left = True
        right = True
        if node is None:
            return True
        if node.left:
            left = node.value <= node.left.value and Heap._is_heap_satisfied(node.left)
        if node.right:
            right = node.value <= node.right.value and Heap._is_heap_satisfied(node.right)
        if left and right:
            return True
        else:
            return False

    @staticmethod
    def swap(n1, n2):
        temp = n2.value
        n2.value = n1.value
        n1.value = temp

    @staticmethod
    def _swap(node):
        if node.left is None and node.right is None:
            return node
        elif node.right is None:
            node.value, node.left.value = node.left.value, node.value
            return node
        else:
            if node.left.value < node.right.value:
                node.value, node.left.value = node.left.value, node.value
                if not Heap._is_heap_satisfied(node.left):
                    Heap._swap(node.left)
            else:
                node.value, node.right.value = node.right.value, node.value
                if not Heap._is_heap_satisfied(node.right):
                    Heap._swap(node.right)

    def insert(self, value):
        '''
        Inserts value into the heap.
        '''
        if self.root is None:
            self.root = Node(value)
            self.root.descendents = 1
        else:
            Heap._insert(value, self.root)

    @staticmethod
    def _insert(value, node):
        '''
        FIXME:
        Implement this function.
        '''
        node.descendents += 1 
        binary = "{0:b}".format(node.descendents)
        if binary[1] == '0':
            if node.left is None:
                node.left = Node(value)
                node.left.descendents = 1
            else:
                Heap._insert(value, node.left)
            if node.value > node.left.value:
                node.value, node.left.value = node.left.value, node.value
        elif binary[1] == '1':
            if node.right is None:
                node.right = Node(value)
                node.right.descendents = 1
            else:
                Heap._insert(value, node.right)
            if node.value > node.right.value:
                node.value, node.right.value = node.right.value, node.value
    
    @staticmethod
    def size(self):
        if self.root is None:
            return 0 
        stack = []
        stack.append(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1 
                stack.append(node.left)
            if node.right:
                size += 1
                stack.append(node.right)
        return size

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.
        '''
        for x in xs:
            self.insert(x)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.

        FIXME:
        Implement this function.
        This function is not implemented in the lecture notes,
        but if you understand the structure of a Heap it should be easy to implement.

        HINT:
        Create a recursive staticmethod helper function,
        similar to how the insert and find functions have recursive helpers.
        '''
        if self.root:
            return Heap._find_smallest(self.root)
    
    @staticmethod
    def _find_smallest(node):
        return node.value

    @staticmethod
    def _remove_last_elem(node):
        binary = "{0:b}".format(node.descendents)
        if len(binary) == 2:
            if binary[1] == '1':
                temp = node.right
                node.right = None
            elif binary[1] == '0':
                temp = node.left
                node.left = None
            return temp.value
        else:
            if binary[1] == '0':
                return Heap._remove_last_elem(node.left)
            elif binary[1] == '1':
                return Heap._remove_last_elem(node.right)
        node.descendents -= 1
    
    def remove_min(self):
        '''
        Removes the minimum value from the Heap. 
        If the heap is empty, it does nothing.

        FIXME:
        Implement this function.
        '''
        self.root.value = Heap._remove_last_element(self.root)
        if not Heap._is_heap_satisfied(self.root):
            Heap._swap(self.root)

    @staticmethod
    def _remove_min(node, size):
        bin_size = str(bin(size))
        bin_size = bin_size[2:]
        if len(bin_size) == 2:
            if bin_size[-1] == '0':
                replace = node.left
                Heap.swap(node, replace)
                node.left = None
            else:
                replace = node.right
                Heap.swap(node, replace)
                node.right = None
        else:
            for num in bin_size[1:-1]:
                if num == '0':
                    node = node.left
                if num == '1':
                    node = node.right
            if bin_size[-1] == '0':
                replace = node.left
                Heap.swap(node, replace)
                node.left = Node
            else:
                replace = node.right
                Heap.swap(node, replace)
                node.right = None
