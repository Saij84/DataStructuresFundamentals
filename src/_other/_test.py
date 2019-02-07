def is_matched(expression):
  opening = tuple('({[')
  closing = tuple(')}]')
  mapping = dict(zip(opening, closing))
  queue = []

  for letter in expression:
    if letter in opening:
      print(mapping[letter])
      queue.append(mapping[letter])
    elif letter in closing:
      print(letter != queue.pop())
      if not queue or letter != queue.pop():
        return False
  print(mapping)
  print(queue)
  return not queue




print(is_matched('[](()'))