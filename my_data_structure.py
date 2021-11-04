class LinkedListNode():
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList ():
  def __init__(self, value):
    self.head = LinkedListNode(value)

  def add(self, value):
    new_node = LinkedListNode(value)
    current_node = self.head
    while current_node.next != None:
      current_node = current_node.next
    current_node.next = new_node
  
  def print(self):
    arr = []
    current_node = self.head
    while current_node != None:
      arr.append(current_node.value)
      current_node = current_node.next
    return arr


class TreeNode:
  def __init__(self, value):
    self.tag = "Node"
    self.value = value
    self.left = None
    self.right = None

class TreeLeaf:
  def __init__(self, value):
    self.tag = "Leaf"
    self.value = value
    self.leaf = None

class Tree:
  def __init__(self):
    self.head = None
  
  def add_leaf(self, value):
    if self.head == None:
      self.head = TreeLeaf(value)
    else:
      pass