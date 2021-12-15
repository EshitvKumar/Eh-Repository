import random
import turtle as tutel
tutel.speed(0)

def moveCursor(pos):
    tutel.penup()
    tutel.goto(pos)
    tutel.pendown()

#initialising parameters
tutel.pensize(10)
height_list = [3, 4, 4, 5, 5, 5, 6, 6, 7]
tutel.color('brown')
tutel.setheading(90)
moveCursor((0, -100))
allleft = []
allright = []
tutel.forward(100)
d = {'left' : [], 'right' : []}

#functions
def createLeaves(pos):
    moveCursor(pos)
    tutel.color('green')
    tutel.fillcolor('green')
    tutel.begin_fill()
    tutel.circle(20)
    tutel.end_fill()



def createTree(i, pos):
    global allright
    global allleft
    ll = []
    rl = []
    if not pos in allleft:
        moveCursor(pos)
        tutel.setheading(90)
        for _ in range(i):
            tutel.left(random.randint(10, 30))
            if tutel.heading() > 180:
                break
            tutel.forward(10 * height_list[random.randrange(len(height_list))])
            ll.append(tutel.position())
            allleft += ll
        ll.pop(-1)

    if not pos in allright:
        moveCursor(pos)
        tutel.setheading(90)
        for _ in range(i):
            tutel.right(random.randint(10, 30))
            if tutel.heading() > 270:
                break
            tutel.forward(10 * height_list[random.randrange(len(height_list))])
            rl.append(tutel.position())
            allright += rl
        rl.pop(-1)
    return ll, rl

#the first two tree branches
d['left'], d['right'] = createTree(5, tutel.position())
allleft += d['left']
allright += d['right']

#formation of tree
for i in [4, 3, 2, 1]:
    r = d['right']
    l = d['left']
    r2, l2 = [], []
    for j in l:
        l2 += createTree(i, j)[1]
    d['right'] = l2
    for j in r:
        r2 += createTree(i, j)[0]
    d['left'] = r2
    allright += d['right']
    allleft += d['left']

allpos = list(set(allright + allleft))
for leaf in allpos:
    createLeaves(leaf)
moveCursor((1000, 1000))
tutel.done()
