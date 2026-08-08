from math import sqrt

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width (self, new_width):
        self.width = new_width

    def set_height (self, new_height):
        self.height = new_height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*(self.width + self.height)
    
    def get_diagonal(self):
        return sqrt(self.width**2 + self.height**2)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return'Too big for picture.'
        else:
            picture = ''
            for line in range(self.height):
                line = self.width * '*' + '\n'
                picture += line
            return picture
    
    def get_amount_inside(self, shape):
        return (self.height // shape.height)*(self.width // shape.width)

class Square(Rectangle):
    def __init__(self, side_length):
        self.side_length = side_length
        super().__init__(side_length, side_length)
    
    def __str__(self):
        return f'Square(side={self.side_length})'
    
    def set_width(self, new_side_length):
        self.side_length = new_side_length
        self.width = new_side_length
        self.height = new_side_length
    
    def set_height(self, new_side_length):
        self.side_length = new_side_length
        self.width = new_side_length
        self.height = new_side_length
    
    def set_side(self, new_side_length):
        self.side_length = new_side_length
        self.width = new_side_length
        self.height = new_side_length