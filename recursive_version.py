import random
from utils import print2D, display, random_rank


class ZipTree:
    def __init__(self, key):
        self.key = key
        self.rank = None
        self.left = None
        self.right = None


def insert(x, root):
    if root is None:
        x.left = x.right = None
        x.rank = random_rank()
        return x
    if x.key < root.key:
        if insert(x, root.left) == x:
            if x.rank < root.rank:
                root.left = x
            else:
                root.left = x.right
                x.right = root
                return x
    else:
        if insert(x, root.right) == x:
            if x.rank <= root.rank:
                root.right = x
            else:
                root.right = x.left
                x.left = root
                return x
    return root

# input left, and right node, and zip them together.
def zip_path(x, y):
    if x is None:
        return y
    if y is None:
        return x
    if x.rank < y.rank:
        y.left = zip_path(x, y.left)
        return y
    else:
        x.right = zip_path(x.right, y)
        return x


def delete(x, root):
    if x.key == root.key:
        return zip_path(root.left, root.right)
    if x.key < root.key:
        if x.key == root.left.key:
            root.left = zip_path(root.left.left, root.left.right)
        else:
            delete(x, root.left)
    else:
        if x.key == root.right.key:
            root.right = zip_path(root.right.left, root.right.right)
        else:
            delete(x, root.right)
    return root


if __name__ == '__main__':
    # zip_tree = ZipTree(6)
    zip_tree = insert(ZipTree(5), None)
    zip_tree = insert(ZipTree(6), zip_tree)
    zip_tree = insert(ZipTree(7), zip_tree)
    zip_tree = insert(ZipTree(8), zip_tree)
    zip_tree = insert(ZipTree(9), zip_tree)
    zip_tree = insert(ZipTree(10), zip_tree)
    # zip_tree = insert(ZipTree(12), zip_tree)
    print("Inserted items with ranks: ")
    display(zip_tree)
    print("Items in tree structure: ")
    print2D(zip_tree)
    zip_tree = delete(ZipTree(8), zip_tree)
    print("Items after deletion: ")
    display(zip_tree)
    print("Items in tree structure: ")
    print2D(zip_tree)
