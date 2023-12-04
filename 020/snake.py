from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTION = {
    'UP': 90,
    'DOWN': 270,
    'LEFT': 180,
    'RIGHT': 0
}


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(
                self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTION['DOWN']:
            self.head.setheading(DIRECTION['UP'])

    def down(self):
        if self.head.heading() != DIRECTION['UP']:
            self.head.setheading(DIRECTION['DOWN'])

    def left(self):
        if self.head.heading() != DIRECTION['RIGHT']:
            self.head.setheading(DIRECTION['LEFT'])

    def right(self):
        if self.head.heading() != DIRECTION['LEFT']:
            self.head.setheading(DIRECTION['RIGHT'])
