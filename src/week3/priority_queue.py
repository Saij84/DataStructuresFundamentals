"""
My implementation of Priority Qeue, using dictionaries
"""

class Priority_Qeue:

    def __init__(self):
        self.qeue = dict()

    def get_qeue(self):
        return self.qeue

    def insert(self, priority, elem):
        if self.qeue.get(priority, False):
            self.qeue[priority].append(elem)
        else:
            self.qeue.update({priority: [elem]})

    def extract_max(self):
        if len(self.qeue) != 0:
            maxKey = max(self.qeue, key=int)
            self.remove_key(maxKey)


    def remove_key(self, key):
        self.qeue.pop(key)
        return "key {} was removed from the qeue"


    def remove_elem(self, key,  elem):
        for i in self.qeue[key]:
            if i == elem:
                self.qeue[key].remove(i)
                return "element {} as removed from {}".format(i, key)


    def get_max(self):
        return max(self.qeue, key=int)


    def change_priority(self, new_prio, elem):
        for key, val in self.qeue.items():
            if len(val) > 1:
                for i in val:
                    if i == elem:
                        if self.qeue.get(new_prio, False):
                            self.qeue[new_prio].append(elem)
                            self.remove_elem(key, elem)
                            return 1
                        else:
                            self.qeue.update({new_prio: [i]})
                            self.remove_elem(key, i)
                            return 1
            else:
                self.remove_key(key)
                self.qeue.update({new_prio: val})


# test data
arr = [(14, 78), (68, 73), (15, 76), (48, 72), (3, 9), (12, 56), (14, 32), (18, 55), (11, 18), (24, 55)]
priorityQeue = Priority_Qeue()

for prio, elem in arr:
    priorityQeue.insert(prio, elem)

print(priorityQeue.get_qeue())
print(priorityQeue.change_priority(98, 78))
print(priorityQeue.get_qeue())