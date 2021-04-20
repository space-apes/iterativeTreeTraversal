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

from BSTADT import BSTADT, BSTNode

class BSTRecur(BSTADT):

    #recursive implementation of insertSingle
    #all nodes are recursively root nodes of their own subtrees.
    def insertSingle(self, curRoot, keyVal):
        if self.root == None:
            self.root = BSTNode(keyVal) 
        else:
            
            if keyVal < curRoot.key:
                if not curRoot.hasLeft():
                    curRoot.left = BSTNode(keyVal)
                else:
                    self.insertSingle(curRoot.left, keyVal)
            else:
                if not curRoot.hasRight():
                    curRoot.right = BSTNode(keyVal)
                else:
                    self.insertSingle(curRoot.right, keyVal)
        return 


    def search(self, curRoot, searchValue):
        if self.isEmpty():
            print('can not search empty BST')
            return False

        if curRoot == None:
            return False 
        elif searchValue == curRoot.key:
            return True
        else: 
            return self.search(curRoot.left, searchValue) or self.search(curRoot.right, searchValue)

    """i don't really understand this even though I coded it. 
    i feel like might have some conditions it doesnt work

    def oldSearch(self, curRoot, searchValue):
        if self.isEmpty():
            print('can not search empty BST')
            return False

        if curRoot == None:
            return False 
        elif searchValue == curRoot.key:
            return True
        elif self.search(curRoot.left, searchValue):
            return True
        elif self.search(curRoot.right, searchValue):
            return True
        else:
            return False
    """

    #print all values following preorder traversal recursively
    def printPreorder(self, curRoot):
        if self.root == None:
            print('empty tree')
            return

        if curRoot == None:
            return 

        print(curRoot.key)
        self.printPreorder(curRoot.left)
        self.printPreorder(curRoot.right)
        
        return 


    #print all values following Inorder traversal recursively
    def printInorder(self, curRoot):
        if self.root == None:
            print('empty tree')
            return

        if curRoot == None:
            return 

        self.printInorder(curRoot.left)
        print(curRoot.key)
        self.printInorder(curRoot.right)
        
        return 


    #print all values following postorder traversal recursively
    def printPostorder(self, curRoot):
        if self.root == None:
            print('empty tree')
            return

        if curRoot == None:
            return 

        self.printPostorder(curRoot.left)
        self.printPostorder(curRoot.right)
        print(curRoot.key)
        
        return 

#open file
#copy each line to string list
#create new BST
#insert all elements of list into BST
#print all key values using various traversal methods
#ask user for search string
#if search string is in BST, print "yes" otherwise print "no"
def main():
    #get contents of file into string list
    stringList = []
    try:
        fo = open('problemExampleData.txt', 'r')
        fileLineBuffer = fo.readline().rstrip('\n')
        while fileLineBuffer != '':
            stringList.append(fileLineBuffer)
            fileLineBuffer = fo.readline().rstrip('\n')
        fo.close()
    except OSError as e:
        print("OS error: "+str(e)) 
    
    #create new BST
    bst = BSTRecur()

    #insert all elements of list into BST
    bst.insertFromStringList(stringList)
    
    print("*****PREORDER RECURSIVE*****")
    bst.printPreorder(bst.root)


    print("*****INORDER RECURSIVE*****")
    bst.printInorder(bst.root)

    print("*****POSTORDER RECURSIVE*****")
    bst.printPostorder(bst.root)

    searchString = input('please enter a city to search for: ')
    print (f'that value is in the BST: {bst.search(bst.root, searchString)}')

if __name__ == "__main__":
    main()
