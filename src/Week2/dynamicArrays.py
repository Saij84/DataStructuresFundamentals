
def get(i):
    if i < 0 or i >= size:
        print("ERROR: index out of range")
    return arr[i]

def set(i, val):
    if i < 0 or i >= size:
        print("ERROR: index out of range")
    arr[i] = val


def push_back():
    if size == capacity:
        new_arr = [0 for i in (capacity*2)]
        for i in range(size-1):
            new_arr[i] = arr[i]



def remove():
    pass