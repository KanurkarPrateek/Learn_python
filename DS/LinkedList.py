class Node:
    def __int__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __int__(self):
        self.head= None
        self.n = 0

    def __len__(self):
        return self.n

L = LinkedList()

print(len(L))