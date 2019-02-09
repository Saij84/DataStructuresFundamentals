# python3

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


class TreeHeight:
    """Computes height of a given tree.
    Height of a (rooted) tree is the maximum depth of a node, or the maximum
    distance from a leaf to the root.
    """

    def __init__(self):
        self.n = 0
        self.parent = []
        self.cache = []

    def read(self):
        """Reads data from standard input."""
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.cache = [0] * self.n

    def path_len(self, node_idx):
        """Returns path length from given node to the root."""
        parent = self.parent[node_idx]

        if parent == -1:
            return 1

        if self.cache[node_idx]:
            return self.cache[node_idx]

        self.cache[node_idx] = 1 + self.path_len(self.parent[node_idx])
        print(self.cache)
        return self.cache[node_idx]

    def compute_height(self):
        """Computes the tree height."""
        return max([self.path_len(i) for i in range(self.n)])


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()