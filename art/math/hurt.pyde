# このコードは、Processingの中にあるPythonモードで実行してください。

xmin = ymin = -1
xmax = ymax = -xmin

def setup():
    global xscl, yscl
    size(800, 800)
    xscl = width / (xmax - xmin)
    yscl = -height / (ymax - ymin)

def draw():
    global xscl, yscl
    background(255)
    translate(width / 2, height / 2)
    printGraphFunction()

def f(x):
    if 1 - 2.8 * x ** 2 >= 0:
        return abs(0.3 * x) ** 0.5 + ((1 - 2.8 * x ** 2) ** 0.5) / 2
    else:
        return 10 * height
def g(x):
    if 1 - 2.8 * x ** 2 >= 0:
        return abs(0.3 * x) ** 0.5 - ((1 - 2.8 * x ** 2) ** 0.5) / 2
    else:
        return 10 * height

def printGraphFunction():
    x = xmin
    while x <= xmax:
        stroke(255, 0, 0)
        strokeWeight(3)
        circle(x * xscl, f(x) * yscl, 1)
        circle(x * xscl, g(x) * yscl, 1)
        x += 0.0001
