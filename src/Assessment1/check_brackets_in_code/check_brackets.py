# python3

from collections import namedtuple
import os

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append((i, next))

        if next in ")]}":
            # Process closing bracket, write your code here
            pass


def main():
    cwd = os.getcwd()
    path = cwd + "\\tests\\"

    for file in os.listdir(path):
        with open(path + file) as inFile:
            text = inFile.read()
            mismatch = find_mismatch(text)
            print(mismatch)



if __name__ == "__main__":
     main()
