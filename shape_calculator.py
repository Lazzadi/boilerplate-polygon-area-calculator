class Rectangle:

  
  def __init__(self, width, height):
    self.width = width
    self.height = height

  
  def set_width(self, width):
    self.width = width

  
  def set_height(self, height):
    self.height = height

  
  def get_area(self):
    return (self.width*self.height)

  
  def get_perimeter(self):
    return (2*self.width + 2*self.height)

  
  def get_diagonal(self):
    return ((self.width**2 + self.height**2)**.5)

    
  def get_picture(self):
    picture = ''
    if(self.width<=50 and self.height<=50):
      for i in range (0, self.height):
        for j in range (0, self.width):
          picture += '*'
        picture += '\n'
      # picture = picture.rstrip('\n')
      return (picture)
    else:
      return('Too big for picture.')

  
  def get_amount_inside(self, shape):
    if (shape.height>self.height or shape.width>self.width):
      return 0
    else:
      return (int(self.height/shape.height) *  int(self.width/shape.width))

  
  def __repr__(self):
    return (f'Rectangle(width={self.width}, height={self.height})')

class Square(Rectangle):
  
  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, newSide):
    self.width = newSide
    self.height = newSide

  def set_width(self, width):
    self.width = width
    self.height = width

  def set_height(self, height):
    self.height = height
    self.width = height    

  def __repr__(self):
    return (f'Square(side={self.width})')



  #TODO: Additionally, the set_width and set_height methods on the Square class should set both the width and height.