"""
Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""
import turtle

#calculate the postition of each car from their trajectory per second
#calculate a raidus of the car where other cars should not come within
sc = turtle.Screen()
t = turtle.Turtle()
car1 = turtle.Turtle()
car2 = turtle.Turtle()
car3 = turtle.Turtle()
car4 = turtle.Turtle()
# car1.speed(0)
# car2.speed(0)
# car3.speed(0)
# car4.speed(0)
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

def set_cars_manually():
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


# SERVER

from math import sqrt

DATA = {"1": [], 
        "2":[],
        "3":[],
        "4":[]}
TRAJECTORIES = {"1": '', 
        "2":'',
        "3":'',
        "4":''}

# FIXME: t is used by global turtle as well as time
def collision(dx, dy, vx, vy, ax, ay, b):
    "Takes position data and a buffer and returns True if there is a collision and False if there isn't"
    if ax == 0 and ay == 0:
        # cubic equation, minimum of dy/dx can be found
        t = (dx*vx+dy*vy)/(vx**2+vy**2)
        if sqrt(dx**2+dx**2+2*(dx*vx+dy*vy)*t+(2*(dx*ax+dy*ay)+dx**2+vy**2)*t**2+2*(vx*ax+vy*ay)*t**3+(ax**2+ay**2)*t**4) < b:
            # collides
            return True
        # does not collide
        return False
    for t in range(0, 100):
        t = t/10
        if sqrt(dx**2+dx**2+2*(dx*vx+dy*vy)*t+(2*(dx*ax+dy*ay)+dx**2+vy**2)*t**2+2*(vx*ax+vy*ay)*t**3+(ax**2+ay**2)*t**4) < b:
        # a collision detected
            return True
    # no collisions detected
    return False

def add_data(car_number, displacement, time):
    "Add data to global variable, where car number is '1' to '4', displacement is a tuple of x and y floats, and time is a float"
    DATA[car_number].append((displacement[0], displacement[1], time))

def get_initial_values(data):
    "Takes a list of displacements and times, then returns the initial displacement, velocity, and acceleration"
    dxlist = [point[0] for point in data]
    dylist = [point[1] for point in data]
    timelist = [point[2] for point in data]
    d = (dxlist[0], dylist[0])
    v = ((dxlist[1]-dxlist[0])/(timelist[1]-timelist[0]), (dylist[1]-dylist[0])/(timelist[1]-timelist[0]))
    v2 = ((dxlist[2]-dxlist[1])/(timelist[2]-timelist[1]), (dylist[2]-dylist[1])/(timelist[2]-timelist[1]))
    a = ((v2[0]-v[0])/(timelist[2]-timelist[0]), (v2[1]-v[1])/(timelist[2]-timelist[0]))
    return d, v, a

def get_trajectory(d, v, a):
    "Given tuples of initial displacement, velocity, and acceleration, return a lambda function for the displacement of the car given time (assuming constant acceleration)"
    return lambda t: (d[0] + v[0]*t + a[0]*t**2, d[1] + v[1]*t + a[1]*t**2)

def _distance(x1, y1, x2, y2):
    "Given two coordinates (or vectors) calculate the distance between them and return it"
    return sqrt((x1-x2)**2+(y1-y2)**2)


def _inbounds(coord):
    return (coord >=-240 and coord <= 240)

def _inbounds_from_list(coordlist):
    "Takes a list of coordinates and returns False if any of them are out of bounds"
    for coord in coordlist:
        if not(_inbounds(coord)):
            return False
    return True

def collision_from_trajectory(f, g, b, step=0.05):
    "Given two displacement functions for the cars, return True if they will come within b units"
    time = 0
    while True:
        time += step
        c1 = f(time)
        c2 = g(time)
        if not(_inbounds_from_list([c1[0], c1[1], c2[0], c2[1]])):
            # out of bounds, break loop
            break
        dist = _distance(c1[0], c1[1], c2[0], c2[1])
        if dist < b:
            return True
    return False

def min_dist(f, g, step=0.05):
    "Given two displacement functions for the cars, return the smallest distance"
    time = 0
    small = float("inf")
    while True:
        time += step
        c1 = f(time)
        c2 = g(time)
        if not(_inbounds_from_list([c1[0], c1[1], c2[0], c2[1]])):
            # out of bounds, break loop
            break
        dist = _distance(c1[0], c1[1], c2[0], c2[1])
        small = min(small, dist)
    return small

def draw_trajectory(id, f, step=0.1):
    time = 0
    while True:
        time += step
        d = f(time)
        if not(_inbounds_from_list([d[0], d[1]])):
            # out of bounds
            break
        stamp_car(id, d[0], d[1])

def draw_trajectories(ids, fs, step=0.1):
    time = 0
    while True:
        for index, num in enumerate(ids):
            time += step
            d = fs[index](time)
            if not(_inbounds_from_list([d[0], d[1]])):
                # out of bounds
                break
            stamp_car(num, d[0], d[1])

def draw(number):
    d, v, a = get_initial_values(DATA[number])
    f = get_trajectory(d, v, a)
    draw_trajectory(number, f)

def draw_multiple(numbers):
    functions = []
    for num in numbers:
        d, v, a = get_initial_values(DATA[num])
        functions.append(get_trajectory(d, v, a))
    print(collision_from_trajectory(functions[0], functions[1], 10))
    print(min_dist(functions[0], functions[1]))
    draw_trajectories(numbers, functions, 0.05)

def getvals_for_stop(v, d):
    'Given current velocity and distance to braking point, find the deceleration and return initial values'
    # using v^2 = v0^2+2ax where v-final velocity, v0-initial velocity, a-constant acceleration, x-change in distacne
    a = ((-v[0]**2)/(2*d[0]), (-v[1]**2)/(2*d[1]))
    # tuple for 2d vector
    return d, v, a


def add_data_and_check(car_number, displacement, time):
    "Add data point, return False if not enough data, True if path works"
    DATA[car_number].append((displacement[0], displacement[1], time))
    if len(DATA[car_number]) == 3:
        # can determine trajectory
        d, v, a = get_initial_values(DATA[car_number])
        f = get_trajectory(d, v, a)
        TRAJECTORIES[car_number] = f
        for i in ['1', '2', '3', '4']:
            if i != car_number and TRAJECTORIES[i] != '':
                check = collision_from_trajectory(f, TRAJECTORIES[i], 10)
                if check: # there is a collision path
                    return getvals_for_stop(v, d) # find values and tell car to slow down (stop by intersection)
        else: # no collision
            return True
    else:
        return False

def remove_trajectory():
    pass # if car is out of bounds (successful intersection), remove its trajectory from global dict


add_data("1", (-230, 20), 0)
add_data("1", (-211, 20), 1)
add_data("1", (-182, 20), 2)

add_data("2", (-20, -230), 0)
add_data("2", (-20, -220), 1)
add_data("2", (-20, -200), 2)

add_data("3", (230, -20), 0)
add_data("3", (211, -19), 1)
add_data("3", (182, -18), 2)

add_data("4", (20, 230), 0)
add_data("4", (20, 220), 1)
add_data("4", (20, 200), 2)

board()
set_cars()


draw_multiple(["1", "2", "3", "4"])
sc.exitonclick()
