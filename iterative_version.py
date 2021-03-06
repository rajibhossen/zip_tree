import random
from utils import print2D, display, random_rank


class ZipTree:
    def __init__(self, key):
        self.key = key
        self.rank = None
        self.left = None
        self.right = None


root = None


def insert(x):
    global root
    node = ZipTree(x)
    rank = random_rank()
    node.rank = rank
    key = node.key
    current = root
    prev = None

    # find the position of item x to be inserted in the left or right subtree,
    # if rank is smaller than current or same rank but key is greater than current
    while current is not None and (rank < current.rank or (rank == current.rank and key > current.key)):
        prev = current
        if key < current.key:
            current = current.left
        else:
            current = current.right
    # if root is none, program didnt enter the while loop. otherwise, finds the appropriate position of new item.
    # current iterate to exact position, prev hold previous current value
    # if rank is greater than root rank, didn't enter while, current will always be root
    if current == root:
        root = node
    elif key < prev.key:
        prev.left = node
    else:
        prev.right = node

    if current is None:
        node.left = None
        node.right = None
        return
    if key < current.key:
        node.right = current
    else:  # item is greater than the root key, all of the current will be left of the item.
        node.left = current

    prev = node

    while current is not None:
        fix = prev
        if current.key < key:
            while True:
                prev = current
                current = current.right
                if current is None or current.key > key:
                    break
        else:
            while True:
                prev = current
                current = current.left
                if current is None or current.key > key:
                    break
        if fix.key > key or (fix == node and prev.key > key):
            fix.left = current
        else:
            fix.right = current


def delete(x):
    global root
    current = root
    prev = None
    while x != current.key: # find the x in the tree
        prev = current
        if x < current.key:
            current = current.left
        else:
            current = current.right
    left = current.left  # get the left and right subtree of x
    right = current.right
    if left is None:
        current = right
    elif right is None: # zipping two path, left and right. if left rank is greater or same, current will be left, else right
        current = left
    elif left.rank >= right.rank:
        current = left
    else:
        current = right
    if root.key == x:
        root = current
    elif x < prev.key:
        prev.left = current
    else:
        prev.right = current

    while left is not None and right is not None:
        if left.rank >= right.rank:
            while True:
                prev = left
                left = left.right
                if left is None or left.rank < right.rank:
                    break
            prev.right = right
        else:
            while True:
                prev = right
                right = right.left
                if right is None or left.rank >= right.rank:
                    break
            prev.left = left


if __name__ == '__main__':
    # zip_tree = ZipTree(6)
    insert(5)
    insert(6)
    insert(7)
    insert(8)
    insert(9)
    insert(10)

    print("Inserted items with ranks: ")
    display(root)
    print("Items in tree structure: ")
    print2D(root)
    delete(8)
    delete(5)
    delete(10)
    # print("Items after deletion: ")
    # display(root)
    # print("Items in tree structure: ")
    # print2D(root)
