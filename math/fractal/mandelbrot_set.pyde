# このコードは、Processingの中にあるPythonモードで実行してください。

xmin = -2.5
ymin = -2
xmax = 1.5
ymax = 2
cnt = 0

def setup():
    global x_size, y_size
    size(700, 700)
    noStroke()
    x_size = float(xmax - xmin) / width
    y_size = float(ymax - ymin) / height

def draw():
    global cnt
    cnt += 1
    for x in range(width):
        for y in range(height):
            z = [(xmin + x * x_size), (ymin + y * y_size)]
            colorNum = getMandelbrot_set(z, 100)
            if colorNum == 100:
                fill(0, 255, 255)
            elif colorNum >= 10:
                fill(0, 0, 255)
            else:
                fill(colorNum * 30, 0, 0)
            rect(x, height - y, 1, 1)

def getAdd(a, b):
    return [a[0] + b[0], a[1] + b[1]]

def getMult(a, b):
    return [a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0]]

def getAbs(a):
    return (a[0] ** 2 + a[1] ** 2) ** 0.5

def getMandelbrot_set(z0, limitNum):
    cnt = 0
    z1 = z0
    while cnt <= limitNum:
        if getAbs(z1) > 2.0:
            return cnt
        z1 = getAdd(getMult(z1, z1), z0)
        cnt += 1
    return limitNum
