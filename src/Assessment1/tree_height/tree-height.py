# python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        # Replace this code with a faster implementation
        maxHeight = 0
        for vertex in range(self.n):
            i = vertex
            maxHeight = max(maxHeight, self.recursion(i))
        return maxHeight

    def recursion(self, i, height=1):
        if self.parent[i] == -1:
            return height
        else:
            return self.recursion(self.parent[i], height+1)


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()
