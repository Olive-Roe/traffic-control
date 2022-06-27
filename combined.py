"""
Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""
import turtle
import time
from time import time as timenow
from math import sqrt

# calculate the postition of each car from their trajectory per second
# calculate a radius of the car where other cars should not come within
sc = turtle.Screen()
t = turtle.Turtle()
car1 = turtle.Turtle()
car2 = turtle.Turtle()
car3 = turtle.Turtle()
car4 = turtle.Turtle()
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
    for i in range(4):
        d()
        t.penup()
        t.forward(40)
        t.left(90)
        t.forward(250)
        t.pendown()
        t.right(270)

    t.penup()
    t.setposition(0, -250)
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
    car1_x = int(
        input("Please enter an x coordiante for car 1 (range -250 to -40): "))
    car2_y = int(
        input("Please enter a y coordinate for car 2 (range -250 to -40): "))
    car3_x = int(
        input("Please enter an x coordinate for car 3 (range 40 to 250): "))
    car4_y = int(
        input("Please enter a y coordinate for car 4 (range 40 to 250): "))

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


ID_TABLE = {"1": car1,
            "2": car2,
            "3": car3,
            "4": car4,
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


# SERVER

DATA = {"1": [],
        "2": [],
        "3": [],
        "4": []}
TRAJECTORIES = {"1": '',
                "2": '',
                "3": '',
                "4": ''}

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
    for t in range(100):
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
    v = ((dxlist[1]-dxlist[0])/(timelist[1]-timelist[0]),
         (dylist[1]-dylist[0])/(timelist[1]-timelist[0]))
    v2 = ((dxlist[2]-dxlist[1])/(timelist[2]-timelist[1]),
          (dylist[2]-dylist[1])/(timelist[2]-timelist[1]))
    a = ((v2[0]-v[0])/(timelist[2]-timelist[0]),
         (v2[1]-v[1])/(timelist[2]-timelist[0]))
    return d, v, a


def get_trajectory(d, v, a):
    "Given tuples of initial displacement, velocity, and acceleration, return a lambda function for the displacement of the car given time (assuming constant acceleration)"
    return lambda t: (d[0] + v[0]*t + a[0]*t**2, d[1] + v[1]*t + a[1]*t**2)


def _distance(x1, y1, x2, y2):
    "Given two coordinates (or vectors) calculate the distance between them and return it"
    return sqrt((x1-x2)**2+(y1-y2)**2)


def _inbounds(coord):
    return (coord >= -240 and coord <= 240)


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
    running = True
    while running:
        for index, num in enumerate(ids):
            time += step
            d = fs[index](time)
            if not(_inbounds_from_list([d[0], d[1]])):
                # out of bounds
                running = False
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


def _divide_without_zde(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return 0


def getvals_for_stop(v, d):
    'Given current velocity and distance to braking point, find the deceleration and return initial values'
    # using v^2 = v0^2+2ax where v-final velocity, v0-initial velocity, a-constant acceleration, x-change in distacne
    a = (_divide_without_zde((-v[0]**2), (4*d[0])),
         _divide_without_zde((-v[1]**2), (4*d[1])))
    # safe division which ignores 0 to account for zero division error
    # tuple for 2d vector
    return d, v, a


def add_data_and_check(car_number, displacement, time):
    "Add data point, return False if not enough data, True if path works"
    if car_number in DATA:
        DATA[car_number].append((displacement[0], displacement[1], time))
    else:
        # does not exist yet, add a new entry
        DATA[car_number] = [(displacement[0], displacement[1], time)]
    if len(DATA[car_number]) == 3:
        # can determine trajectory
        d, v, a = get_initial_values(DATA[car_number])
        f = get_trajectory(d, v, a)
        TRAJECTORIES[car_number] = f
        print(d, v, a, TRAJECTORIES, DATA)
        print(
            f"d:{d}, v:{v}, a:{a}, traj:{TRAJECTORIES[car_number]}, data:{DATA[car_number]}")
        for i in ['1', '2', '3', '4']:
            if i != car_number and TRAJECTORIES[i] != '':
                # there is a collision path
                if collision_from_trajectory(f, TRAJECTORIES[i], 10):
                    DATA[car_number] = []  # reset data as trajectory changes
                    # find values and tell car to slow down (stop by intersection)
                    return getvals_for_stop(v, closest_braking(d))
        else:  # no collision
            return True
    else:
        return False


def remove_trajectory():
    # if car is out of bounds (successful intersection), remove its trajectory from global dict
    pass


def closest_braking(disp):
    "Given a displacement, calculate the nearest distance to the closest braking point"
    x, y = disp
    closest = float("inf")
    # braking points are (-40, 20), (40, 20), (20, 40), (-20, -40)
    # beginning of intersection
    for tup in [(-40, 20), (40, 20), (20, 40), (-20, -40)]:
        x1, y1 = tup
        d = _distance(x, y, x1, y1)
        if d < closest:
            closest = d
            output = (x1-x, y1-y)
    return output


CARS = {}


class Car:
    def __init__(self, name, direction, d, v, a, color="red"):
        # d, v, a refer to initial displacement, velocity, and acceleration
        self.turtle = turtle.Turtle()
        self.turtle.color(color)
        self.turtle.setheading(direction)
        # 0 down, 90 right, 180 up, 270 left
        # 0 right, 90 up, 180 left, 270 down
        self.name = name
        CARS[name] = self
        self.x, self.y = d
        self.d = d
        self.v = v
        self.current_v = v
        self.a = a
        self.traj = get_trajectory(d, v, a)

    def display_trajectory(self):
        draw_trajectory(self.name, self.traj)

    def update_trajectory(self):
        self.traj = get_trajectory(self.d, self.v, self.a)

    def measure(self):
        result = add_data_and_check(self.name, (self.x, self.y), time.time())
        if result not in [True, False]:
            # there is a collision path, follow braking trajectory
            d, v, a = result
            self.a = a
            self.update_trajectory()
            print("braking", self.d, self.v, self.a)
        print("going", self.d, self.v, self.a)

    def brake(self):
        d, v, a = getvals_for_stop(
            self.current_v, closest_braking((self.x, self.y)))
        print(closest_braking((self.x, self.y)))
        self.a = a
        self.update_trajectory()
        print("braking", (self.x, self.y), self.v, self.a)

    def goto(self, time):
        x, y = self.traj(time)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.x = x
        self.y = y
        self.current_v = (self.v[0] + self.a[0]*time,
                          self.v[1] + self.a[1]*time)


def run_cars(start=0, stop=10, step=0.05):
    time = start
    measures = 0
    last = timenow()
    CARS["5"].brake()
    while time < stop:
        # if measures < 3 and timenow() > last+1:
        #     CARS["5"].measure()
        #     CARS["6"].measure()
        #     measures += 1
        #     last = timenow()
        for car_id in CARS:
            car = CARS[car_id]
            car.goto(time)
        time += step
    print(CARS["5"].x)


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
# set_cars()

c1 = Car("5", 0, (-230, 20), (19, 0), (10, 0), "magenta")
c2 = Car("6", 270, (20, 230), (0, -10), (0, -10), "red")
run_cars(0, 20)

#draw_multiple(["1", "2", "3", "4"])
sc.exitonclick()
