import sys
import math
import time
import random
sys.setrecursionlimit(10 ** 9)


class BSTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class AVLNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1
### AVL ###
class AVL:
    def insertAVL(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.val:
            root.left = self.insertAVL(root.left, key)
        else:
            root.right = self.insertAVL(root.right, key)
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def preorder(self, root):
        global orders
        if not root:
            return
        orders.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        global orders
        if root:
            self.inorder(root.left)
            orders.append(root.val)
            self.inorder(root.right)
    def postorder(self, root):
        global orders
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            orders.append(root.val)
    def searchAVL(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self.searchAVL(root.left, key)
        else:
            return self.searchAVL(root.right, key)

    def deleteNode(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                tmp = root.right
                root = None
                return tmp
            elif root.right is None:
                tmp = root.left
                root = None
                return tmp

            tmp = self.searchMin(root.right)
            root.val = tmp.val
            root.right = self.deleteNode(root.right, tmp.val)
        return root

    def searchMin(self, root):
        global droga
        while root.left != None:
            droga.append(root.val)
            root = root.left
        return root

    def searchMax(self, root):
        global droga
        while root.right != None:
            droga.append(root.val)
            root = root.right
        return root

    def deleteAVL(self, root):
        if root is None:
            return None
        self.deleteAVL(root.left)
        self.deleteAVL(root.right)

### BST ###
class BST:
    def insertBST(self, root, node):
        if root is None:
            root = node
        else:
            if root.val < node.val:
                if root.right is None:
                    root.right = node
                else:
                    self.insertBST(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insertBST(root.left, node)
        return root

    def searchBST(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self.searchBST(root.left, key)
        else:
            return self.searchBST(root.right, key)

    def searchMin(self, root):
        global droga
        while root.left != None:
            droga.append(root.val)
            root = root.left
        return root

    def searchMax(self, root):
        global droga
        while root.right != None:
            droga.append(root.val)
            root = root.right
        return root

    def inorder(self, root):
        global orders
        if root:
            self.inorder(root.left)
            orders.append(root.val)
            self.inorder(root.right)

    def postorder(self, root):
        global orders
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            orders.append(root.val)

    def preorder(self, root):
        global orders
        if root:
            orders.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def deleteBST(self,root):
        if (root is None):
            return None
        self.deleteBST(root.left)
        self.deleteBST(root.right)

    def deleteNode(self,root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                tmp = root.right
                root = None
                return tmp
            elif root.right is None:
                tmp = root.left
                root = None
                return tmp

            tmp = self.searchMin(root.right)
            root.val = tmp.val
            root.right = self.deleteNode(root.right, tmp.val)
        return root


    def rotateRight(self, root, top):
        if top.left is None:
            return root, top
        node = top.left
        top.left = node.right
        if node.right:
            node.right = top
        node = top
        if top is None:
            root = node
        elif top == top.right:
            top.right = node
        else:
            top.left = node
        node.right = top
        top = node
        return root, node

    def rotateLeft(self, root, top):
        if top.right is None:
            return root, top
        node = top.right
        top.right = node.left
        if node.left:
            node.left = top
        node = top
        if top is None:
            root = node
        elif top == top.left:
            top.left = node
        else:
            top.right = node
        node.left = top
        top = node
        return root, node

    def backbone(self, root, top):
        parent = top
        left_child = None
        while parent:
            left_child = parent.left
            if left_child:
                root = self.rotateRight(root, parent)
                parent = left_child
            else:
                parent = parent.right
            return root
    def perfect_tree(self, root, n):
        root = self.backbone(root, root)
        m = int(pow(2, math.floor(math.log(n+1, 2))) - 1)
        root = self.makeRotations(root, n-m)
        while m > 1:
            m //= 2
            root = self.makeRotations(root, m)
        return root
    def makeRotations(self, root, x):
        p = root
        for i in range(x):
            if p:
                root = self.rotateLeft(root, p)
                if p:
                    p = p.right
        return root

def random_arr():
    start_rand_arr = []
    for i in range(1000000):
        random_number = random.randint(1, 100000)
        if random_number not in start_rand_arr:
            start_rand_arr.append(random_number)
    return start_rand_arr

### DRIVER CODE ###

droga = []
orders = []
#start_random_array = random_arr()
array = []

while True:
    print("PLease decide from what source you want me to read data:")
    print("Write \"txt\" to read from Sort.txt file")
    print("Write \"key\" to read from keyboard")
    type_of_action = input()
    if type_of_action == "key":
        print("Give me an array pls:")
        array = input().split()
        try:
            array = list(map(int, array))
            break
        except ValueError:
            print("Array must contain valid values!")
    elif type_of_action == "txt":
        a = open("Sort.txt", "r")
        a = a.read()
        array = a.split()
        try:
            array = list(map(int, array))
            break
        except ValueError:
            print("Array must contain valid values!")
    else:
        print("Please, try again")
        continue

# BUILD BST FOR THE FRIST TIME
BST_tree = BST()
root_bst = None
start_build_bst = time.perf_counter()
for i in range(0,len(array)):
    root_bst = BST_tree.insertBST(root_bst, BSTNode(array[i]))
build_bst_time = time.perf_counter() - start_build_bst

AVL_tree = AVL()
root_avl = None
start_build_avl = time.perf_counter()
for i in range(0,len(array)):
    root_avl = AVL_tree.insertAVL(root_avl, array[i])
build_avl_time = time.perf_counter() - start_build_avl

while True:
    print("Please decide what kind of tree you want to build from input data:")
    print("1.BST \n2.AVL\n3.Time of building trees\n4.Exit Program")
    tree_decision = input()
    try:
        tree_decision = int(tree_decision)
    except ValueError:
        print("PLEASE INSERT CORRECT NUMBER")
    if tree_decision > 4 and tree_decision < 1:
        print("PLEASE INSERT CORRECT NUMBER")

    # BST TREE
    if tree_decision == 1:
        print("Please decide what you want to do and enter correct number:")
        print("1.Search for min and max value of a Binary Search Tree")
        print("2.Delete an element of a tree by given key")
        print("3.Print the tree inorder")
        print("4.Print the tree preorder")
        print("5.Delete all tree in postorder")
        print("6.Print out in preorder subtree of given key")
        print("7.Balance the tree")
        print("8.Rebuild BST form input array")
        print("9.Exit the program")
        bst = input()
        try:
            bst = int(bst)
        except ValueError:
            print("GIVE ME A CORRECT NUMBER")
        if bst < 1 or bst > 9:
            print("GIVE ME A CORRECT NUMBER")

        # OPTIONS
        if bst == 1:
            start_search_bst = time.perf_counter()
            print("Min:", BST_tree.searchMin(root_bst).val)
            print("I searched minimum for:", time.perf_counter() - start_search_bst)
            for element in droga:
                print(element, end=' ')
            print()
            droga = []
            print("Max:", BST_tree.searchMax(root_bst).val)
            for element in droga:
                print(element, end=' ')
            print()
            droga = []
        elif bst == 2:
            print("Please give me the number of key you want to delete:")
            k_num = input()
            try:
                k_num = int(k_num)
            except ValueError:
                print("GIVE ME A CORRECT NUMBER")
            print("Give me the keys you want to delete")
            keys = input().split()
            try:
                keys = list(map(int, keys))
            except ValueError:
                print("Keys must be correct values")
            for key in keys:
                BST_tree.deleteNode(root_bst, key)
        elif bst == 3:
            inorder_time_start_bst = time.perf_counter()
            BST_tree.inorder(root_bst)
            print("I printed for:", time.perf_counter() - inorder_time_start_bst)
            for element in orders:
                print(element, end=' ')
            print()
            orders = []
        elif bst == 4:
            BST_tree.preorder(root_bst)
            for element in orders:
                print(element, end=' ')
            print()
            orders = []
        elif bst == 5:
            BST_tree.deleteBST(root_bst)
            root_bst = None
            print("Tree deleted")
        elif bst == 6:
            print("Enter the key:")
            k = input()
            try:
                k = int(k)
            except ValueError:
                print("GIVE ME A CORRECT INTEGER")
            BST_tree.preorder(BST_tree.searchBST(root_bst, k))
            for element in orders:
                print(element, end=' ')
            print()
            orders = []
        elif bst == 7:
            BST_tree.perfect_tree(root_bst,len(array))
            print("Tree is balanced now")
        elif bst == 8:
            BST_tree = BST()
            root_bst = None
            for i in range(0, len(array)):
                root_bst = BST_tree.insertBST(root_bst, BSTNode(array[i]))
        elif bst == 9:
            print("Bye bye")
            break

    # AVL TREE
    if tree_decision == 2:
        print("Please decide what you want to do and enter correct number:")
        print("1.Search for min and max value of a AVL Tree")
        print("2.Delete an element of a tree by given key")
        print("3.Print the tree inorder")
        print("4.Print the tree preorder")
        print("5.Delete all tree in preorder")
        print("6.Print out in preorder subtree of given key")
        print("7.Exit the program")
        avl = input()
        try:
            avl = int(avl)
        except ValueError:
            print("GIVE ME A CORRECT NUMBER")
        if avl < 1 or avl > 9:
            print("GIVE ME A CORRECT NUMBER")

        # OPTIONS
        if avl == 1:
            start_search_avl = time.perf_counter()
            print("Min:", AVL_tree.searchMin(root_avl).val)
            print("I searched minimum for:", time.perf_counter() - start_search_avl)
            for element in droga:
                print(element, end=' ')
            print()
            droga = []
            print("Max:", AVL_tree.searchMax(root_avl).val)
            for element in droga:
                print(element, end=' ')
            print()
            droga = []
        elif avl == 2:
            print("Please give me the number of key you want to delete:")
            k_num = input()
            try:
                k_num = int(k_num)
            except ValueError:
                print("GIVE ME A CORRECT NUMBER")
            print("Give me the keys you want to delete")
            keys = input().split()
            try:
                keys = list(map(int, keys))
            except ValueError:
                print("Keys must be correct values")
            for key in keys:
                AVL_tree.deleteNode(root_avl, key)
        elif avl == 3:
            inorder_time_start_avl = time.perf_counter()
            AVL_tree.inorder(root_avl)
            print("I for for:", time.perf_counter() - inorder_time_start_avl)
            for element in orders:
                print(element, end=' ')
            print()
            orders = []
        elif avl == 4:
            AVL_tree.preorder(root_avl)
            for element in orders:
                print(element, end=' ')
            print()
            orders = []
        elif avl == 5:
            AVL_tree.deleteAVL(root_avl)
            root_avl = None
            print("Tree deleted")
        elif avl == 6:
            print("Enter the key:")
            k = input()
            try:
                k = int(k)
            except ValueError:
                print("GIVE ME A CORRECT INTEGER")
            AVL_tree.preorder(AVL_tree.searchAVL(root_avl,k))
            for element in orders:
                print(element, end=' ')
            print()
            orders = []
        elif avl == 7:
            print("Bye bye")
            break
    if tree_decision == 3:
        print("BST build time:", build_bst_time)
        print("AVL build time:", build_avl_time)
    if tree_decision == 4:
        print("Bye bye")
        break
