# queue is initially empty
Queue = {'front': None, 'back': None}


# we will use a node to keep track of the elements
# in the queue which is represented by a linked list
class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next

  def __repr__(self):
    return "{}, {}".format(self.data, self.next)

# add elements to queue in O(1) time


def Enqueue(Queue, element):
  N = Node(element, None)
  if Queue['back'] == None:
    Queue['front'] = N
    Queue['back'] = N
  else:
    Queue['back'].next = N
    Queue['back'] = Queue['back'].next


# remove first element from queue in O(1) time
def Dequeue(Queue):
  if Queue['front'] != None:
    first = Queue['front']
    Queue['front'] = Queue['front'].next
    return first.data
  else:
    if Queue['back'] != None:
      Queue['back'] = None
    return 'Cannot dequeue because queue is empty'


for letter in 'testing the queue':
  Enqueue(Queue, letter)

#Dequeue(Queue)

print(Queue)