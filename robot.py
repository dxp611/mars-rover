class Robot:
  def __init__(self, x, y, orientation):
    self.x = x
    self.y = y
    self.orientation = orientation
    self.lost = False

  def move_forward(self):
    if self.orientation == 'N':
      self.y += 1
    if self.orientation == 'E':
      self.x +=1
    if self.orientation == 'S':
      self.y -= 1
    if self.orientation == 'W':
      self.x -= 1
  
  def rotate_left(self):
    rotate_left_map = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
    self.orientation = rotate_left_map[self.orientation]
  
  def rotate_right(self):
    rotate_right_map = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    self.orientation = rotate_right_map[self.orientation]

  def set_lost(self):
    self.lost = True
