'''
This file implements the Binary Search Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree file.
'''

from Trees.BinaryTree import BinaryTree, Node

class BST():
    '''
    FIXME:
    BST is currently not a subclass of BinaryTree.
    You should make the necessary changes in the class declaration line above 
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the BST.
        '''


    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command BST([1,2,3])
        it's __repr__ will return "BST([1,2,3])"

        For the BST, type(self).__name__ will be the string "BST",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of BST will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__+'('+str(self.to_list('inorder'))+')'


    def is_bst_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether insert/delete functions
        are actually working.
        '''
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        '''
        FIXME:
        Implement this method.
        The lecture videos have the exact code you need,
        except that their method is an instance method when it should have been a static method.
        '''
        l_check = True 
        r_check = True
        if node.left:
            l_check = node.value > node.left.value and BST._is_bst_satisfied(node.left)
        if node.right:
            r_check = node.value < node.right.value and BST._is_bst_satisfied(node.right)
        return l_check and r_check

    def insert(self, value):
        '''
        Inserts value into the BST.
        '''
        if self.root is None:
            self.root = Node(value)
        else:
            BST._insert(value, self.root)

    @staticmethod
    def _insert(value, node):
        '''
        FIXME:
        Implement this function.
        The lecture videos have the exact code you need,
        except that their method is an instance method when it should have been a static method.
        '''
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                BST._insert(value, node.left)

        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                BST._insert(value, node.right)
        else:
            print("Value is already within tree")

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.
        '''
        for i in xs:
            self.insert(i)

    def __contains__(self, value):
        return self.find(value)

    def find(self, value):
        '''
        Returns whether value is contained in the BST.
        '''
        if self.root:
            if BST._find(value, self.root):
                return True
        else:
            return False


    @staticmethod
    def _find(value, node):
        '''
        FIXME:
        Implement this function.
        The lecture videos have the exact code you need,
        except that their method is an instance method when it should have been a static method.
        '''
        if value > node.value and node.right:
            return BST._find(value, node.right)
        elif value < node.value and node.left:
            return BST._find(value, node.left)
        if value == node.value:
            return True
        else:
            return False

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.

        FIXME:
        Implement this function.
        This function is not implemented in the lecture notes,
        but if you understand the structure of a BST it should be easy to implement.

        HINT:
        Create a recursive staticmethod helper function,
        similar to how the insert and find functions have recursive helpers.
        '''
        node = self.root
        return BST._find_smallest(node)
    
    @staticmethod
    def _find_smallest(node):
        if node.left:
            return BST._find_smallest(node.left)
        else:
            return node.value

    def find_largest(self):
        '''
        Returns the largest value in the tree.

        FIXME:
        Implement this function.
        This function is not implemented in the lecture notes,
        but if you understand the structure of a BST it should be easy to implement.
        '''
        node = self.root
        return BST._find_largest(node) 

    @staticmethod
    def _find_largest(node):
        if node.right:
            return BST._find_largest(node.right) 
        else:
            return node.value

    def remove(self,value):
        '''
        Removes value from the BST. 
        If value is not in the BST, it does nothing.

        FIXME:
        implement this function.
        There is no code given in any of the lecture videos on how to implement this function,
        but the video by HMC prof Colleen Lewis explains the algorithm.

        HINT:
        You must have find_smallest/find_largest working correctly 
        before you can implement this function.

        HINT:
        Use a recursive helper function.
        '''
        self.root = BST._remove(self.root,value)

    @staticmethod
    def _remove(node, value):
        if not node:
            return node
    
        if node.value < value:
            node.right = BST._remove(node.right, value)
        elif node.value > value:
            node.left = BST._remove(node.left, value)
        else:
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            
            c = node.right
            while c.left:
                c = c.left
            node.value = c.value
            node.right = BST._remove(node.right, node.value)
        return node

    def remove_list(self, xs):
        '''
        Given a list xs, remove each element of xs from self.

        FIXME:
        Implement this function.
        '''
        for i in xs:
            self.remove(i)
