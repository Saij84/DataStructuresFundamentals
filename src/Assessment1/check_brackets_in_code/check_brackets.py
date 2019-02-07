# python3

from collections import namedtuple
import os
import logging
logger = logging.getLogger(__name__)


Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
        opening_brackets_stack = []
        for i, next in enumerate(text,start=1):
            if next in "([{":
                # Process opening bracket, write your code here
                opening_brackets_stack.append((next, i))

            if next in ")]}":
                # Process closing bracket, write your code here
                if not opening_brackets_stack:
                    return i
                elif are_matching(opening_brackets_stack[-1][0], next):
                    opening_brackets_stack.pop()
        if len(opening_brackets_stack) > 0:
            return opening_brackets_stack[0][1]
        else:
            return "Success"

def main():

    files = r"C:\tools\DataStructuresFundamentals\src\Assessment1\check_brackets_in_code\tests"
    file_num = 29

    with open(files + "\{:02}".format(file_num)) as inFile:
        text = inFile.read()
        mismatch = find_mismatch(text)
        print(mismatch)

if __name__ == "__main__":
     main()
