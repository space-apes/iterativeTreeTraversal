"""
Brian Smith
CSUDH Spring 2021
CSC521 Dr. Tang
Programming Project 3: BST Traversal
"""

"""
    NONFUNCTIONAL REQUIREMENTS:
        -implement BST as ADT
        -implement traversal algorithms both iteratively and recursively 

    FUNCTIONAL REQUIREMENTS:
        - read each string from input file
        - insert contents of each line into BST
        - print contents of BST in each of the following orders:
            - preorder
            - inorder
            - postorder
        - prompt user for search string
        - if search string was key in BST display "yes" otherwise display "no"
        -
"""

class BSTADT():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    #inserts new node in top-down fashion by comparing key values
    def insertSingle(self, curRoot, keyVal):
        #defined in child class
        pass

    def search(self, curRoot, searchValue):
        #defined in child class
        pass

    #inserts multiple nodes from string list 
    def insertFromStringList(self, stringList):
        for x in stringList:
            self.insertSingle(self.root, x)

        return

    #print all values following preorder traversal
    def printPreorder(self, curRoot):
        #defined in child class
        pass

    #print all values following preorder traversal
    def printInorder(self, curRoot):
        #defined in child class
        pass

    #print all values following preorder traversal
    def printPostorder(self, curRoot):
        #defined in child class
        pass
    
class BSTNode:
    def __init__(self, keyVal): 
        self.key = keyVal
        self.left = None
        self.right = None

    def hasChildren(self):
        return self.left != None and self.right != None
    def hasLeft(self):
        return self.left != None
    def hasRight(self):
        return self.right != None


