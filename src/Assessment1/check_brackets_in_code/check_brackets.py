# python3

from collections import namedtuple
import os

Bracket = namedtuple("Bracket", ["char", "position"])




def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    closing_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append((next, i))

        if next in ")]}":
            # Process closing bracket, write your code here
            closing_brackets_stack.append((next, i))

    print(opening_brackets_stack)
    print(closing_brackets_stack)
    compair_stack = zip(reversed(opening_brackets_stack), closing_brackets_stack)
    # for opening, closing in compair_stack:
    #     print(opening[0], closing[0])
    #     #if opening[0] == closing[0]:



def main():
    cwd = os.getcwd()
    path = cwd + "\\tests\\"
    file = r"C:\tools\DataStructuresFundamentals\src\Assessment1\check_brackets_in_code\tests\47"
    # for file in os.listdir(path):
    #     with open(path + file) as inFile:
    #         text = inFile.read()
    #         mismatch = find_mismatch(text)
    #         print(mismatch)

    with open(file) as inFile:
        text = inFile.read()
        mismatch = find_mismatch(text)
        print(mismatch)

if __name__ == "__main__":
     main()
