import random

COUNT = [5]


def print2DUtil(root, space):
    # Base case
    if (root == None):
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(str(root.key)+" ("+str(root.rank)+")")

    # Process left child
    print2DUtil(root.left, space)


# Wrapper over print2DUtil()
def print2D(root):
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)


def display(root):
    if root is None:
        return
    display(root.left)
    print(root.key, root.rank)
    display(root.right)


# def random_rank():
#     number_of_heads = 0
#     while random.uniform(0, 1) < 0.5:
#         number_of_heads += 1
#     return number_of_heads
def random_rank():
    number_of_heads = 0
    while True:
        head_tail = random.randint(0, 1)
        if head_tail == 1:  # heads up
            number_of_heads += 1
        else:  # tail up, return total heads
            break
    return number_of_heads
