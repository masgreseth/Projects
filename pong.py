import turtle, random
turtle.title('Ping Pong')
turtle.bgcolor('#043927')

def draw_scoreboard(player1_points, player2_points):
    redbox = turtle.Turtle()
    redbox.penup()
    redbox.speed(0)
    redbox.setpos(430, 955)
    redbox.shape('square')
    redbox.color('red')
    redbox.turtlesize(3)
    bluebox = turtle.Turtle()
    bluebox.penup()
    bluebox.speed(0)
    bluebox.setpos(510, 955)
    bluebox.shape('square')
    bluebox.color('blue')
    bluebox.turtlesize(3)
    text = turtle.Turtle()
    text.ht()
    text.color('white')
    text.penup()
    text.setpos(416, 920)
    text.write(str(player1_points) + '    ' + str(player2_points), font=['Arial', 28, 'normal'])

class Paddle(turtle.Turtle):
    def __init__(self, xpos, ypos, yvel):
        turtle.Turtle.__init__(self)
        self.yvel = yvel
        self.points = 0
        self.left(90)
        self.penup()
        self.speed(0)
        self.setpos(xpos, ypos)

    def moveup(self):
        if self.ycor() < 1000:
            yp = self.ycor() + self.yvel
        else:
            yp = self.ycor()
        xp = self.xcor()
        self.setpos(xp, yp)

    def movedown(self):
        if self.ycor() > 10:
            yp = self.ycor() - self.yvel
        else:
            yp = self.ycor()
        xp = self.xcor()
        self.setpos(xp, yp)

class Ball(turtle.Turtle):
    def __init__(self, xpos, ypos, xvel, yvel):
        turtle.Turtle.__init__(self)
        self.xv = xvel
        self.yv = yvel
        self.player1_points = 0
        self.player2_points = 0
        self.onscreen = True
        self.left(90)
        self.penup()
        self.speed(0)
        self.setpos(xpos, ypos)
        self.shape('circle')
        self.color('white')

    def moveball(self, player1, player2):
        if self.xv > 0 and self.xcor() > 945:
            if self.ycor() < player2.ycor() + 35 and self.ycor() > player2.ycor() - 35:
                self.xv *= -1
                self.yv = random.randint(-3, 3)
            else:
                self.player1_points += 1
                self.onscreen = False
                draw_scoreboard(self.player1_points, self.player2_points)
                self.ht()
        if self.xv < 0 and self.xcor() < 35:
            if self.ycor() < player1.ycor() + 35 and self.ycor() > player1.ycor() - 35:
                self.xv *= -1
                self.yv = random.randint(-3, 3)
            else:
                self.player2_points += 1
                self.onscreen = False
                draw_scoreboard(self.player1_points, self.player2_points)
                self.ht()
        if self.yv > 0 and self.ycor() > 970:
            self.yv = -1 * self.yv
        if self.yv < 0 and self.ycor() < 20:
            self.yv = -1 * self.yv
        xp = self.xcor() + self.xv
        yp = self.ycor() + self.yv
        self.setpos(xp, yp)

class Game():
    def __init__(self):
        turtle.setworldcoordinates(0, 0, 1000, 1000)
        turtle.delay(0)
        self.player1 = Paddle(-20, 500, 25)
        self.player1.shape('square')
        self.player1.color('red')
        self.player1.turtlesize(3)
        self.player2 = Paddle(1000, 500, 25)
        self.player2.shape('square')
        self.player2.color('blue')
        self.player2.turtlesize(3)
        self.ball_list = []
        for i in range(20):
            self.ball = Ball(500, 500, 12, random.randint(-3, 3))
            self.ball.ht()
            self.ball_list.append(self.ball)
        self.ball_list[0].showturtle()
        draw_scoreboard(self.ball.player1_points, self.ball.player2_points)

        self.gameloop()
        turtle.onkeypress(self.player2.moveup, 'Up')
        turtle.onkeypress(self.player2.movedown, 'Down')
        turtle.onkeypress(self.player1.moveup, 'w')
        turtle.onkeypress(self.player1.movedown, 's')
        turtle.listen()
        turtle.mainloop()

    def gameloop(self):
            if self.ball_list[0].onscreen:
                self.ball_list[0].moveball(self.player1, self.player2)
                turtle.ontimer(self.gameloop, 30)
            else:
                self.ball_list[1].player1_points = self.ball_list[0].player1_points
                self.ball_list[1].player2_points = self.ball_list[0].player2_points
                self.ball_list = self.ball_list[1:]
                self.ball_list[0].showturtle()
                turtle.ontimer(self.gameloop, 200)
            if self.ball_list[0].player1_points == 10:
                print('RED WINS!')
                for ball in self.ball_list:
                    ball.onscreen = False
            if self.ball_list[0].player2_points == 10:
                print('BLUE WINS!')
                for ball in self.ball_list:
                    ball.onscreen = False

Game()
