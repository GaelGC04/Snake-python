from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        super().__init__()
        self.body = []
        self.create()
        self.head = self.body[0]

    # create snake's body
    def create(self):
        for part in range((len(START_POSITIONS))):
            new_part = Turtle()
            new_part.color("white")
            new_part.shape("square")
            new_part.speed("fastest")
            new_part.penup()
            new_part.goto(START_POSITIONS[part])
            self.body.append(new_part)

    # move the snake 20 px forward
    def move(self):
        for part in range((len(self.body) - 1), 0, -1):
            position_x = self.body[part - 1].xcor()
            position_y = self.body[part - 1].xcor()
            self.body[part].goto(position_x, position_y)
        self.head.forward()

