class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Circle"

class ShapeDecorator(Shape):
    def __init__(self, decorated_shape):
        self.decorated_shape = decorated_shape

    def draw(self):
        return self.decorated_shape.draw()

class ColorDecorator(ShapeDecorator):
    def __init__(self, decorated_shape, color):
        super().__init__(decorated_shape)
        self.color = color

    def draw(self):
        return f"{super().draw()} ({self.color} color)"

class BorderDecorator(ShapeDecorator):
    def draw(self):
        return f"{super().draw()} with border"

if __name__ == "__main__":
    circle = Circle()
    print(f"My Shape: {circle.draw()}")

    red_circle = ColorDecorator(circle, "Red")
    print(f"My Shape: {red_circle.draw()}")

    red_border_circle = BorderDecorator(red_circle)
    print(f"My Shape: {red_border_circle.draw()}")