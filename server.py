from math import sqrt
import main

DATA = {"1": [], 
        "2":[],
        "3":[],
        "4":[]}

def collision(dx, dy, vx, vy, ax, ay, b):
  "Takes position data and a buffer and returns True if there is a collision and False if there isn't"
  if ax == 0 and ay == 0:
    # cubic equation, minimum of dy/dx can be found
    t = (dx*vx+dy*vy)/(vx**2+vy**2)
    if sqrt(dx**2+dx**2+2*(dx*vx+dy*vy)*t+(2*(dx*ax+dy*ay)+dx**2+vy**2)*t**2+2(vx*ax+vy*ay)*t**3+(ax**2+ay**2)*t**4) < b:
      # collides
      return True
    # does not collide
    return False
  for t in range(0, 10, 0.1):
    if sqrt(dx**2+dx**2+2*(dx*vx+dy*vy)*t+(2*(dx*ax+dy*ay)+dx**2+vy**2)*t**2+2(vx*ax+vy*ay)*t**3+(ax**2+ay**2)*t**4) < b:
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


def collision_from_trajectory(f, g, b):
  "Given two displacement functions for the cars, return whether they will come between b units for any point in time"
  for t in range(0, 10, 0.1):
    c1 = f(t)
    c2 = g(t)
    if _distance(c1[0], c1[1], c2[0], c2[1]) < b:
      return True
  return False

add_data("1", (-230, 20), 0)
add_data("1", (-220, 20), 1)
add_data("1", (-200, 20), 2)

d, v, a = get_initial_values(DATA["1"])
f = get_trajectory(d, v, a)
main.draw_trajectory("1", f)

main.test("hi")

# main.board()
# main.set_cars()