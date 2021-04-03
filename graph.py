# Note:
# __init__ di objek itu konstruktor
# '__' di depan variabel itu artinya private (khusus python)
# 'self' itu mirip dengan 'this'
# Coba cek 'a star algorithm' di geekforgeeks

class Coordinate:
    # Private
    __x_pos = None # Float
    __y_pos = None # Float

    # Public
    def __init__(self, x_pos, y_pos):
        self.__x_pos = x_pos
        self.__y_pos = y_pos

    def getX(self):
        return self.__x_pos

    def getY(self):
        return self.__y_pos

    def setX(self, x_pos):
        self.__x_pos = x_pos

    def setY(self, y_pos):
        self.__y_pos = y_pos

class Vertice:
    # Private
    __name = None # String
    __coordinate = None # Objek Coordinate
    __parent = None # String
    __fn = None # Float

    # Public
    def __init__(self, name, x_pos, y_pos, parent, fn):
        self.__name = name
        self.__coordinate = Coordinate(x_pos, y_pos)
        self.__parent = parent
        self.__fn = fn

    def getName(self):
        return self.__name

    def getCoordinate(self):
        return self.__coordinate

    def getParent(self):
        return self.__parent

    def getFn(self):
        return self.__fn

    def setName(self, name):
        self.__name = name

    def setCoordinate(self, x_pos, y_pos):
        self.__coordinate = Coordinate(x_pos, y_pos)

    def setParent(self, parent):
        self.__parent = parent

    def setFn(self, fn):
        self.__fn = fn

    def resetVertice(self):
        self.__parent = ""
        self.__fn = 0

class Graph:
    # Private
    __vertices = None # Array of objek Vertice
    __adj_matrix = None # Array of float

    # Public
    def __init__(self, file_name):
        self.__vertices = []
        self.__adj_matrix = []
        
        file = open(file_name, 'r')

        vertices_count = int(file.readline())
        for i in range(vertices_count):
            line = file.readline()
            vertice_name = ""
            vertice_x = ""
            vertice_y = ""

            for j in range(len(line)):
                if line[j] != '(':
                    vertice_name += line[j]
                else:
                    break

            for j in range(j + 1, len(line)):
                if line[j] != ',':
                    vertice_x += line[j]
                else:
                    break

            for j in range(j + 1, len(line)):
                if line[j] != ')':
                    vertice_y += line[j]
                else:
                    break

            while (vertice_name[len(vertice_name) - 1] == ' '):
                vertice_name = vertice_name[:-1]
            vertice_x = float(vertice_x)
            vertice_y = float(vertice_y)
            
            self.__vertices.append(Vertice(vertice_name, vertice_x, vertice_y, "", 0))

        for i in range(vertices_count):
            line = file.readline()
            row = [float(x) for x in line.split(" ")]
            self.__adj_matrix.append(row)

        file.close()

    def getVertices(self):
        return self.__vertices

    def getAdjMatrix(self):
        return self.__adj_matrix

    def aStarPath(self, from_vertice, to_vertice):
        path = []
        return path

graph = Graph("test.txt")
vertices = graph.getVertices()
for i in range(len(vertices)):
    print(vertices[i])
    print(vertices[i].getName())
    print(vertices[i].getCoordinate().getX())
    print(vertices[i].getCoordinate().getY())
    print(vertices[i].getParent())
    print(vertices[i].getFn())
print(graph.getAdjMatrix())