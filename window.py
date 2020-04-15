import turtle

wn = turtle.Screen()
wn.title("Flappy Bird by OEZDEUM")
wn.bgcolor("blue")
wn.bgpic("background.gif")
wn.setup(width=500, height=800)
wn.tracer(0)

wn.register_shape("bird.gif")


class Pipe_bottom(turtle.Turtle):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.dx = -2.5
        self.dy = 0

        super().__init__()
        super().speed(0)
        super().penup()
        super().color(self.color)
        super().shape("square")
        super().shapesize(stretch_wid=32, stretch_len=3, outline=None)
        super().goto(self.x, self.y)

    def reset(self, x, y):
        super().goto(x, y)

    def move(self):
        x = super().xcor()
        x += self.dx
        super().setx(x)

        if super().xcor() < -280:
            return True
        else:
            return False


class Pipe_top(Pipe_bottom):
    def __init__(self, pipe_bottom):
        self.x = pipe_bottom.xcor()
        self.y = pipe_bottom.ycor() + 800
        self.color = pipe_bottom.color

        super().__init__(self.x, self.y, self.color)

    def reset(self, pipe_bottom):
        x = pipe_bottom.xcor()
        y = pipe_bottom.ycor() + 800

        super().goto(x, y)


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        super().speed(0)
        super().penup()
        super().color("yellow")
        super().shape("bird.gif")
        super().goto(-200, 0)
        self.dx = 0
        self.dy = 1
        self.gravity= -0.1

    def go_up(self):
        self.dy += 2

        if self.dy > 10:
            self.dy = 10

    def reset(self):
        super().goto(-200, 0)
        self.dy = 0

    def move(self):
        # Add gravity
        self.dy += self.gravity
        # Move player
        y = super().ycor()
        y += self.dy
        super().sety(y)
        # Bottom Border
        if super().ycor() < -320:
            self.dy = 0
            super().sety(-320)
        # Top Border
        if super().ycor() > 320:
            self.dy = 0
            super().sety(320)


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        super().speed(0)
        super().hideturtle()
        super().penup()
        super().color("white")
        super().goto(0, 250)
        self.score = 0

    def write(self):
        super().write(self.score, move=False, align="left", font=("Arial", 32, "normal"))

    def reset(self):
        self.score = 0
        super().clear()
        self.write()

    def add_score(self):
        self.score += 1
        super().clear()
        self.write()
