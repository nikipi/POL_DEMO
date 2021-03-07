import random
import math

class Location():

  def __init__(self):
    self.random_location()
    self.step_size = 0.01

  def random_location(self):
    self.x = random.random()
    self.y = random.random()

  def random_move(self):
    self.set_x(self.x + self.step_size * (random.random() - 0.5))
    self.set_y(self.y + self.step_size * (random.random() - 0.5))

  def distance(self, other):
    return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

  def move_towards(self, other):
    delta = self.distance(other)
    if delta > 0.0:
      self.set_x(self.x + (other.x - self.x) / delta * self.step_size)
      self.set_y(self.y + (other.y - self.y) / delta * self.step_size)

  def move_angle(self, degrees):
    radius = degrees * math.pi / 180
    dx = math.cos(radius)
    dy = math.sin(radius)
    self.set_x(self.x + dx * self.step_size)
    self.set_y(self.y + dy * self.step_size)

  def get_x(self):
    return self.x

  def get_y(self):
    return self.y

  def set_x(self, x):
    if x > 1.0:
      x = 1.0
    elif x < 0.0:
      x = 0.0
    self.x = x

  def set_y(self, y):
    if y > 1.0:
      y = 1.0
    elif y < 0.0:
      y = 0.0
    self.y = y

  def set_step_size(self, step_size):
    self.step_size = step_size

  def __repr__(self):
    return "({}, {})".format(self.x, self.y)

