import copy
import random

class Hat:
  def __init__(self, **kwargs):
    self.contents = [(k) for k,v in kwargs.items() for x in range(v)]

  def draw(self, num_to_draw):
    if num_to_draw >= len(self.contents):
      return self.contents
    else:
      drawnBalls = []
      for x in range(0, num_to_draw):
        randBall = random.randint(0, len(self.contents)-1)
        drawnBalls.append(self.contents.pop(randBall))
      return drawnBalls
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expectationMet = 0
  for i in range(0, num_experiments):
    exHat = copy.deepcopy(hat)
    drawn = exHat.draw(num_balls_drawn)
    failureMet = False
    for k,v in expected_balls.items():
      if drawn.count(k) < v:
        failureMet = True
    if failureMet == False:
      expectationMet += 1
  return expectationMet/num_experiments