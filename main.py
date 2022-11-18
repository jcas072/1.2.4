#-----import statements-----
import turtle as trtl
import random as rand

#-----initialize turtle-----
walls = trtl.Turtle()
mazerunner = trtl.Turtle()

#-----game configuration----
wallLength = 20 # The max the wall should be
walls.speed(0)

doorLength = 15
barrierLength = 30

#mazerunner.hideturtle()
#-----game functions--------
def drawDoor(x):
  walls.forward(x)
  walls.penup()
  walls.forward(doorLength)
  walls.pendown()

def drawBarrier(y):
  walls.forward(y)
  walls.left(90)
  walls.forward(barrierLength)
  walls.back(barrierLength)
  walls.right(90)

def runnerDown():
  mazerunner.setheading(270)

def runnerUp():
  mazerunner.setheading(90)

def runnerLeft():
  mazerunner.setheading(180)

def runnerRight():
  mazerunner.setheading(0)

def runnerMove():
  mazerunner.forward(7)


for i in range(25): #Makes the walls
  walls.left(90)
  if i < 1: # plain wall
    walls.forward(wallLength)
  elif i < 5: # wall with door
    x = rand.randint(0,wallLength-doorLength)
    drawDoor(x)
    walls.forward(wallLength-x-doorLength)
  else: # wall with door & barrier
    if rand.randint(0,1) == 1:
      x = rand.randint(0,wallLength-doorLength)
      drawDoor(x)
      y = rand.randint(0,wallLength-doorLength-x)
# Makes the barrier
      drawBarrier(y)
# Barrier Done
      walls.forward(wallLength-x-y-doorLength)
    else:
      y = rand.randint(0,wallLength-doorLength)
# Makes the barrier
      drawBarrier(y)
# Barrier Done
      x = rand.randint(0,wallLength-doorLength-y)
      drawDoor(x)
      walls.forward(wallLength-x-y-doorLength)
  wallLength += 15
walls.hideturtle()



#-----events----------------
wn = trtl.Screen()

wn.onkeypress(runnerDown, 's')
wn.onkeypress(runnerUp, 'w')
wn.onkeypress(runnerRight, 'd')
wn.onkeypress(runnerLeft, 'a')
wn.onkeypress(runnerMove, 'g')

wn.listen()
wn.mainloop()