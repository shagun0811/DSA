class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None
        self.n = 0

    def insert_tail(self, value):
        # new node
        new_node = node(value)

        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node

        # increment n
        self.n = self.n + 1

    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
          result = result + str(curr.data) + ','
          curr = curr.next
        return result[:-1]
    def insert_mid(self,after,value):
        new_node = node(value)
        curr = self.head
        while curr != None:
          if curr.data == after:
            break
          curr = curr.next
        if curr != None:
          new_node.next = curr.next
          curr.next = new_node
          self.n = self.n + 1
        else:
          return 'Item not found'
    def remove(self,value):
        if self.head == None:
          return 'Empty'
        if self.head.data == value:
          return self.delete_head()
        curr = self.head
        while curr.next != None:
          if curr.next.data == value:
            break
          curr = curr.next
        if curr.next == None:
          return 'Not Found'
        else:
          curr.next = curr.next.next
          self.n = self.n - 1
    def clear(self):
        self.head = None
        self.n = 0
L_L = linked_list()
for i in range(10):
    L_L.insert_tail(i)
print(L_L)
L_L.insert_mid(8,12)
print(L_L)
L_L.remove(8)
print(L_L)