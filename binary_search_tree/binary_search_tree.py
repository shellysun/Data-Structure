class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # get the value in a BinarySearchTree
    new_tree = BinarySearchTree(value)
    # check the new node's value <= current node's value
    if value < self.value:
      # if there is no left child there already, place the new node
      if not self.left:
        self.left = new_tree
      # there is a node there
      else:
        # repeat the whole process!
        self.left.insert(value)
    # the value >= cureent value
    else:
        if not self.right:
          self.right = new_tree
        else:
          self.right.insert(value)

  def contains(self, target):
    # check if the value of current node matches the target, we're done
    if self.value == target:
      return True
    # if value < the current node's value, call contains on the left subtree
    if target < self.value:
      # check if self.left exists
      if self.left:
        if self.left.contains(target):
          return True
    else:
      if self.right:
        if self.right.contains(target):
          return True
      # doens't contain the target
    return False

  def get_max(self):
    # go only the right side and no child
    # no point in doing anything if our tree is empty
    if not self:
      return None
    # check to see if it has right side, if not, just return that value
    if not self.right:
      return self.value
    # we still have more right children, keep doing it (call get_max())
    return self.right.get_max()
