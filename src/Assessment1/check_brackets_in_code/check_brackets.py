# python3

from collections import namedtuple
import os
import logging
logger = logging.getLogger(__name__)


Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    print(left, right)
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    if len(text.strip()) > 1:
        opening_brackets_stack = []
        for i, next in enumerate(text):
            if next in "([{":
                print(next)
                # Process opening bracket, write your code here
                opening_brackets_stack.append(next)
            if next in ")]}":
                # Process closing bracket, write your code here
                if not opening_brackets_stack or are_matching(opening_brackets_stack[-1], next):
                    return False
        return "Success"
    else:
        return 1

def main():

    files = r"C:\tools\DataStructuresFundamentals\src\Assessment1\check_brackets_in_code\tests"
    file_num = 2

    with open(files + "\{:02}".format(file_num)) as inFile:
        text = "[](())" #inFile.read()
        mismatch = find_mismatch(text)
        print(mismatch)

if __name__ == "__main__":
     main()
