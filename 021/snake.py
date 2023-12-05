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
        self.init_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def init_snake(self):
        self.create_snake()
        self.head = self.segments[0]

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.init_snake()

    def extend(self):
        self.add_segment(self.segments[-1].position())

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
