# このコードは、Processingの中にあるPythonモードで実行してください。
xmin = -1
xmax = 1
ymin = -1
ymax = 1

rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600, 600)
    xscl = width / rangex
    yscl = - height / rangey

def draw():
    global xscl, yscl
    background(255)
    translate(width / 2, height / 2)
    grid()
    graphFunction()
    
def g(x):
    if 1 - 2.8 * x ** 2 >= 0:
        return abs(0.3 * x) ** 0.5 + ((1 - 2.8 * x ** 2) ** 0.5) / 2
    else:
        return 1000
def h(x):
    if 1 - 2.8 * x ** 2 >= 0:
        return abs(0.3 * x) ** 0.5 - ((1 - 2.8 * x ** 2) ** 0.5) / 2
    else:
        return 1000

def graphFunction():
    x = xmin
    while x <= xmax:
        fill(0)
        circle(x * xscl, g(x) * yscl, 1)
        circle(x * xscl, h(x) * yscl, 1)
        x += 0.0001

def grid():
    strokeWeight(1)
    stroke(0, 255, 255)
    for i in range(xmin, xmax + 1):
        line(i * xscl, ymin * yscl, i * xscl, ymax * yscl)
    for i in range(ymin, ymax + 1):
        line(xmin * xscl, i * yscl, xmax * xscl, i * yscl)
    stroke(0, 0, 0)
    line(xmin * xscl, 0, xmax * xscl, 0)
    line(0, ymin * yscl, 0, ymax * yscl)
