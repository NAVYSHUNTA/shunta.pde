# このコードは、Processingの中にあるPythonモードで実行してください。
xmin = ymin = -10
xmax = ymax = -xmin

def setup():
    size(800, 800)
    global xscl, yscl
    xscl = width / (xmax - xmin)
    yscl = -height / (ymax - ymin)
    noFill()

def draw():
    global xscl, yscl
    background(255)
    translate(width / 2, height / 2)
    theta_x = map(mouseX, 0, width, 0, TWO_PI)
    theta_y = map(mouseY, 0, height, 0, TWO_PI)
    rotation_matrix = [[cos(theta_x), -sin(theta_x)], [sin(theta_y), cos(theta_y)]]
    printGrid(xscl, yscl)
    i = [[0, 0], [1, 0], [1, 3], [0, 3]]
    i_point = [[0, 4], [1, 4], [1, 5], [0, 5]]
    n = [[2, 5], [2, 0], [3, 0], [3, 2.5], [4, 3.5], [5, 3], [5, 0], [6, 0], [6, 3.5], [5, 4.5], [4, 5], [3, 4], [3, 5]]
    input_matrix = [i, i_point, n]
    strokeWeight(5)
    fill(255, 0, 0)
    for input_vector in input_matrix:
        printGraph(input_vector)
    fill(0, 0, 255)
    for input_vector in input_matrix:
        output_matrix = getTransposeMatrix(getMatrixMultiplication(rotation_matrix, getTransposeMatrix(input_vector)))
        printGraph(output_matrix)

def getTransposeMatrix(matrix):
    t_matrix = [[] for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            t_matrix[i].append(matrix[j][i])
    return t_matrix


def printGraph(matrix):
    beginShape()
    for pt in matrix:
        vertex(pt[0] * xscl, pt[1] * yscl)
    endShape(CLOSE)

def printGrid(xscl, yscl):
    strokeWeight(1)
    stroke(0, 255, 255)
    for i in range(xmin, xmax + 1):
        line(i * xscl, ymin * yscl, i * xscl, ymax * yscl)
    for i in range(ymin, ymax + 1):
        line(xmin * xscl, i * yscl, xmax * xscl, i * yscl)
    stroke(0)
    line(0, ymin * yscl, 0, ymax * yscl)
    line(xmin * xscl, 0, xmax * xscl, 0)

def getMatrixAddition(matrix_a, matrix_b):
    matrix = []
    for i in range(len(matrix_a)):
        matrix_row = []
        for k in range(len(matrix_a[0])):
            matrix_row.append(matrix_a[i][k] + matrix_b[i][k])
        matrix.append(matrix_row)
    return matrix

def getMatrixMultiplication(matrix_a, matrix_b):
    matrix = []
    for i in range(len(matrix_a)):
        matrix_row = []
        for j in range(len(matrix_b[0])):
            sum_row = 0
            for k in range(len(matrix_a[0])):
                sum_row += matrix_a[i][k] * matrix_b[k][j]
            matrix_row.append(sum_row)
        matrix.append(matrix_row)
    return matrix
