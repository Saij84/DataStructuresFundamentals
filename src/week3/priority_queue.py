class Priority_Qeue:
    def __init__(self):
        self.qeue = dict()

    def insert(self, priority, elem):
        if self.qeue.get(priority, False):
            self.qeue[priority].append(elem)
        else:
            self.qeue.update({priority: [elem]})

    def extract_max(self):
        if self.qeue:
            maxElem = max(self.qeue, key=int)
            self.remove(maxElem)

    def remove(self, elem):
        for key, val in self.qeue.items():
            if val == elem:
                self.qeue.pop(key)
                print("({}: {}) was removed".format(key, val))
                break

    def get_max(self):
        return max(self.qeue, key=int)

    def change_priority(self, elem, new_prio):
        for key, val in self.qeue.items():
            if val == elem:
                self.qeue.pop(key)
                self.qeue.update({new_prio: val})

arr = [(14, 78), (68, 73), (15, 76), (48, 72), (3, 9), (12, 56), (14, 32), (18, 55), (11, 18), (24, 55)]
priorityQeue = Priority_Qeue()


for prio, elem in arr:
    priorityQeue.insert(prio, elem)

print(priorityQeue.change_priority(32, 19))