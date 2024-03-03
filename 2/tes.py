class Node:
   def __init__(self, data, next_node=None):
      self.data = data
      self.next = next_node

class linkedList:
   def __init__(self):
      self.head = None

   def add_node(self, data):
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node
   
   def display(self):
      if self.head is None:
         print("Linked list is empty")
      else:
         data = self.head
         while data is not None:
            print(data.data, "======>", end=" ")
            data = data.next

objek = linkedList()
objek.add_node(1)
objek.add_node(2)
objek.add_node(3)
objek.add_node(10)
objek.add_node(1389394234809)
objek.display()
