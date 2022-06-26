"""
Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""
import turtle
import time
#calculate the postition of each car from their trajectory per second
#calculate a raidus of the car where other cars should not come within
sc = turtle.Screen()
t = turtle.Turtle()
car1 = turtle.Turtle()
car2 = turtle.Turtle()
car3 = turtle.Turtle()
car4 = turtle.Turtle()
car1.speed(0)
car2.speed(0)
car3.speed(0)
car4.speed(0)
car1.color("red")
car2.color("blue")
car3.color("orange")
car4.color("magenta")

def board():
  t.speed(0)
  t.penup()
  t.setposition(-40, -250)
  t.pendown()
  def lane():
    t.left(90)
    t.forward(190)
    t.circle(20, 90)
    t.forward(190)
    t.right(90)
  for i in range(4):
    lane()
    t.penup()
    t.forward(80)
    t.right(180)
    t.pendown()
  
  t.penup()
  t.setposition(0, -250)
  t.pendown()
  def d():
    t.left(90)
    t.forward(210)
  for i in range (4):
    d()
    t.penup()
    t.forward(40)
    t.left(90)
    t.forward(250)
    t.pendown()
    t.right(270)

  t.penup()
  t.setposition(0,-250)
  t.pendown()
  def grass():
    t.penup()
    t.backward(40)
    t.left(90)
    t.pendown()
    t.color("green")
    t.begin_fill()
    t.forward(190)
    t.circle(20, 90)
    t.forward(190)
    t.left(90)
    t.forward(210)
    t.left(90)
    t.forward(210)
    t.end_fill()

  for i in range(4):
    grass()
    t.penup()
    t.left(90)
    t.forward(250)
    t.left(90)
    t.forward(210)
    t.left(90)
    t.pendown()
  t.color("black")
  t.hideturtle()
  t.speed(1)


def t_lights():
  light1 = turtle.Turtle()
  light1.color("green")
  time
    time.time()
    s = time.time()
    e = time.time()
    num1 = e-s
    if num1%5 == 0 and num1%10 == 0:
      c = green
      light1.color(c)
    elif num1%5==0:
      c = red
      light.color(c)
    
    
def set_cars():
  car1.penup()
  car1.setposition(-250, 20)
  car1.pendown()
  car2.penup()
  car2.left(90)
  car2.setposition(-20, -250)
  car2.pendown()
  car3.penup()
  car3.setposition(250, -20)
  car3.left(180)
  car3.pendown()
  car4.penup()
  car4.setposition(20, 250)
  car4. right(90)
  car4.pendown()
  
  car1_x = int(input("Please enter an x coordiante for car 1 (range -250 to -40): "))
  car2_y = int(input("Please enter a y coordinate for car 2 (range -250 to -40): "))
  car3_x = int(input("Please enter an x coordinate for car 3 (range 40 to 250): "))
  car4_y = int(input("Please enter a y coordinate for car 4 (range 40 to 250): "))
  
  car1.penup()
  car1.setposition(car1_x, 20)
  car1.pendown()
  car2.penup()
  car2.setposition(-20, car2_y)
  car2.pendown()
  car3.penup()
  car3.setposition(car3_x, -20)
  car3.pendown()
  car4.penup()
  car4.setposition(20, car4_y)
  car4.pendown()

ID_TABLE = {"1":car1,
           "2":car2,
           "3":car3,
           "4":car4,
           }

def set_car(id, x, y):
  car = ID_TABLE[id]
  car.penup()
  car.setpos(x, y)
  car.pendown()

def stamp_car(id, x, y):
  car = ID_TABLE[id]
  car.penup()
  car.setpos(x, y)
  car.pendown()
  car.stamp()

def draw_trajectory(id, f, start=0, stop=10, step=0.1):
  for t in range(start, stop, step):
    disp = f(t)
    stamp_car(id, disp[0], disp[1])
    
def test(a):
  print(a)

def set_custom_cars(x1, y1, x2, y2, x3, y3, x4, y4):
  car1.penup()
  car1.setposition(x1, y1)
  car1.pendown()
  car2.penup()
  car2.setposition(x2, y2)
  car2.pendown()
  car3.penup()
  car3.setposition(x3, y3)
  car3.pendown()
  car4.penup()
  car4.setposition(x4, y4)
  car4.pendown()

def speed_cars():
  car1_speed = int(input("Please give a speed for car 1 from range 1 to 5: "))
  car2_speed = int(input("Please give a speed for car 1 from range 1 to 5: "))
  car3_speed = int(input("Please give a speed for car 1 from range 1 to 5: "))
  car4_speed = int(input("Please give a speed for car 1 from range 1 to 5: "))
  
  
  car1_speed = car1_speed/10000000000000000
  car2_speed = car1_speed/10000000000000000
  car3_speed = car1_speed/10000000000000000
  car4_speed = car1_speed/10000000000000000
  
  car1.speed(car1_speed)
  car1.forward(100)
  car2.speed(car2_speed)
  car2.forward(100)
  car3.speed(car3_speed)
  car3.forward(100)
  car4.speed(car4_speed)
  car4.forward(100)


board()
#set_cars()
