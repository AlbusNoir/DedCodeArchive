import turtle

# set up
screen = turtle.Screen()
screen.screensize(300, 300)
screen.title('PyLogo')
screen.bgcolor('black')

logo = turtle.Turtle()
logo.hideturtle()
logo.color('white')  # blue - #03A9FA yellow - #FFEB3B
logo.speed('fastest')


# move func
def move_to(coord):
    logo.penup()
    logo.goto(coord)
    make_square()


# square func
def make_square():
    logo.pendown()
    side = 20
    for _ in range(4):
        logo.forward(side)
        logo.left(90)


# set lists
blue = (
    (-75, -50), (-100, -50),
    (-125, -25), (-100, -25), (-75, -25),
    (-125, 0), (-100, 0), (-75, 0),
    (-125, 25), (-100, 25), (-75, 25),
    (-125, 50), (-100, 50), (-75, 50), (-50, 50), (-25, 50), (0, 50), (25, 50), (50, 50), (75, 50), (100, 50),
    (-125, 75), (-100, 75), (-75, 75), (-50, 75), (-25, 75), (0, 75), (25, 75), (50, 75), (75, 75), (100, 75),
    (50, 100), (75, 100), (100, 100),
    (-25, 125), (0, 125), (25, 125), (50, 125), (75, 125), (100, 125),
    (-25, 150), (25, 150), (50, 150), (75, 150), (100, 150),
    (-25, 175), (0, 175), (25, 175), (50, 175), (75, 175), (100, 175)
)

# yellow will come in opposite dir of blue, because aesthetics
yellow = (
    (150, 125), (125, 125),
    (175, 100), (150, 100), (125, 100),
    (175, 75), (150, 75), (125, 75),
    (175, 50), (150, 50), (125, 50),
    (175, 25), (150, 25), (125, 25), (100, 25), (75, 25), (50, 25), (25, 25), (0, 25), (-25, 25), (-50, 25),
    (175, 0), (150, 0), (125, 0), (100, 0), (75, 0), (50, 0), (25, 0), (0, 0), (-25, 0), (-50, 0),
    (0, -25), (-25, -25), (-50, -25),
    (75, -50), (50, -50), (25, -50), (0, -50), (-25, -50), (-50, -50),
    (75, -75), (25, -75), (0, -75), (-25, -75), (-50, -75),
    (75, -100), (50, -100), (25, -100), (0, -100), (-25, -100), (-50, -100)
)

eyes = (
    (0, 150), (50, -75)
)

'''
# origin placeholder - used in original positioning
logo.goto(0, 0)
make_square()
'''

# center should be roughly origin
for coord in blue:
    logo.color('#03A9FA')
    move_to(coord)

for coord in yellow:
    logo.color('#FFEB3B')
    move_to(coord)

for coord in eyes:
    logo.color('white')
    move_to(coord)


def write_things(word):
    logo.penup()
    logo.goto(-75, -150)
    logo.pendown()
    font = ('Serif', '31')
    logo.color('white')
    logo.write(word, font=font)


write_things('Python')

screen.exitonclick()

'''IDEA:

goto somewhere
define font="font" "size"
write color,font'''
