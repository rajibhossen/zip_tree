# A python implementation of the Zip Tree. 

A zip tree is a binary search tree in which each node has a rank and the tree is (max)-heap-ordered with respect to ranks, with rank ties broken in favor of smaller keys. The details of the tree is available at https://arxiv.org/pdf/1806.06726.pdf

File Structure:
- iterative_verison.py - Iterative Implementation of insertion and deletion
- recursive_version.py - recursive implementation of insertion and deletion
- utils.py - Contains random rank generator, pretty print the tree

Instructions to run:
Main functions contains demo data for insertion and deletion. Feel Free to change the data. Implemented in Python 3.7

    python3 iterative_version.py
    python3 recursive_version.py