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

class BSTIter(BSTADT):

    #iterative implementation of insertSingle
    def insertSingle(self, curRoot, keyVal):
        if self.root == None:
            self.root = BSTNode(keyVal) 
        else:
            while True:
                if keyVal < curRoot.key:
                    if curRoot.hasLeft():
                        curRoot = curRoot.left
                    else:
                        curRoot.left = BSTNode(keyVal)
                        return
                else:
                    if curRoot.hasRight():
                        curRoot = curRoot.right
                    else:
                        curRoot.right = BSTNode(keyVal)
                        return
   
    def search(self, curRoot, searchValue):
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

#print all values following preorder traversal iteratively
    def printPreorder(self, curRoot):
        if self.root == None:
            print('empty tree')
            return
        
        nodeStack = []
        nodeStack.append(curRoot)
        
        while len(nodeStack) > 0:
            curNode = nodeStack.pop()
            print(curNode.key)
            if curNode.hasRight():
                nodeStack.append(curNode.right)
            if curNode.hasLeft():
                nodeStack.append(curNode.left)

    #print all values following inorder traversal iteratively 
    def printInorder(self, curNode):
        if self.root == None:
            print('empty tree')
            return

        nodeStack = []
        nodeStack.append(curNode)
        
        while len(nodeStack) > 0:
            if curNode == None:
                curNode = nodeStack.pop()
                print(curNode.key)
                curNode = curNode.right
            else:
                nodeStack.append(curNode)
                curNode = curNode.left
                    

#print all values following postorder traversal iteratively
    #visit whole left subtree
    #visit whole right subtree
    #visit root

    def printPreordertPostorder(self, curNode):
        if self.root == None:
            print('empty tree')
            return

    nodeStack = []
    nodeStack.append(curNode)

    while current != None or len(nodeStack) > 0:
        if curNode == None:
            if nodeStack[len(nodeStack)+1].hasRight():
                curNode = nodeStack
            else:
                curNode = nodeStack.pop()
                print(curNode.key)
        else:
            nodeStack.append(curNode)
            curNode = curNode.left
            #stuff 



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
    bst = BSTIter()

    #insert all elements of list into BST
    bst.insertFromStringList(stringList)
    
    print("*****PREORDER ITERATIVE*****")
    bst.printPreorder(bst.root)


    print("*****INORDER ITERATIVE*****")
    bst.printInorder(bst.root)
"""
    print("*****POSTORDER RECURSIVE*****")
    bst.printPostorder(bst.root)

    searchString = input('please enter a city to search for: ')
    print (f'that value is in the BST: {bst.search(bst.root, searchString)}')
"""

if __name__ == "__main__":
    main()
