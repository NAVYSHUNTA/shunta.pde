# このコードは、Processingの中にあるPythonモードで実行してください。

t = 0

def setup():
    size(600, 600)
    rectMode(CENTER)
    colorMode(HSB)

def draw():
    global t
    background(255)
    translate(width / 2, height / 2)
    for i in range(360):
        rotate(radians(1))
        pushMatrix()
        translate(200, 0)
        rotate(radians(t + ((mouseX // 60) % 10) * i))
        stroke(255 * i / 360, 255, 255)
        printTriangle(100)
        popMatrix()
    t += 0.5

def printTriangle(length):
    noFill()
    triangle(0, -length, length * sqrt(3) / 2, length / 2, -length * sqrt(3) / 2, length / 2)
