# Note:
# __init__ di objek itu konstruktor
# 'self' itu mirip dengan 'this'
# Kalau mau copy object, pakai deepcopy

from math import radians, cos, sin, asin, sqrt
import copy

class Coordinate:
    # Private
    __lat = None # Float
    __long = None # Float

    # Public
    def __init__(self, lat, long):
        self.__lat = lat
        self.__long = long

    def getLat(self):
        return self.__lat

    def getLong(self):
        return self.__long

    def setLat(self, lat):
        self.__lat = lat

    def setLong(self, long):
        self.__long = long

class Vertice:
    # Private
    __name = None # String
    __coordinate = None # Objek Coordinate
    # __parent = None # Int
    # __fn = None # Float
    # __gn = None # Float

    # Public
    def __init__(self, name, lat, long):
        self.__name = name
        self.__coordinate = Coordinate(lat, long)
        # self.__parent = parent
        # self.__fn = fn
        # self.__gn = gn

    def getName(self):
        return self.__name

    def getCoordinate(self):
        return self.__coordinate

    # def getParent(self):
    #     return self.__parent

    # def getFn(self):
    #     return self.__fn

    # def getGn(self):
    #     return self.__gn

    def setName(self, name):
        self.__name = name

    def setCoordinate(self, lat, long):
        self.__coordinate = Coordinate(lat, long)

    # def setParent(self, parent):
    #     self.__parent = parent

    # def setFn(self, fn):
    #     self.__fn = fn

    # def setGn(self, gn):
    #     self.__gn = gn

    # def resetVertice(self):
    #     self.__parent = -1
    #     self.__gn = 0

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
            vertice_lat = ""
            vertice_long = ""

            for j in range(len(line)):
                if line[j] != '(':
                    vertice_name += line[j]
                else:
                    break

            for j in range(j + 1, len(line)):
                if line[j] != ',':
                    vertice_lat += line[j]
                else:
                    break

            for j in range(j + 1, len(line)):
                if line[j] != ')':
                    vertice_long += line[j]
                else:
                    break

            while (vertice_name[len(vertice_name) - 1] == ' '):
                vertice_name = vertice_name[:-1]
            vertice_lat = float(vertice_lat)
            vertice_long = float(vertice_long)
            
            self.__vertices.append(Vertice(vertice_name, vertice_lat, vertice_long))

        for i in range(vertices_count):
            line = file.readline()
            row = [float(x) for x in line.split(" ")]
            self.__adj_matrix.append(row)

        file.close()

    def getVertices(self):
        return self.__vertices

    def getAdjMatrix(self):
        return self.__adj_matrix

    def getVerticeByName(self, name):
        for vertice in self.__vertices:
            if vertice.getName() == name:
                return vertice
        return None

    def getVerticeByIndex(self, idx):
        return self.__vertices[idx]

    def getVerticeIndex(self, name):
        for i in range(len(self.__vertices)):
            if self.__vertices[i].getName() == name:
                return i
        return None

    # Yang ini buat testing aja
    # Buat ngitung heuristiknya
    def euclideanDistance(self, from_vertice_lat, from_vertice_long, to_vertice_lat, to_vertice_long):
        return ((from_vertice_lat - to_vertice_lat) ** 2 + (from_vertice_long - to_vertice_long) ** 2) ** 0.5

    # Ini buat ngitung jarak antar dua titik di bumi (dalam meter)
    # Buat ngitung heuristiknya
    def haversine(self, from_vertice_lat, from_vertice_long, to_vertice_lat, to_vertice_long):
        from_vertice_lat, from_vertice_long, to_vertice_lat, to_vertice_long = map(radians, [from_vertice_lat, from_vertice_long, to_vertice_lat, to_vertice_long])
        dlon = to_vertice_long - from_vertice_long
        dlat = to_vertice_lat - from_vertice_lat 
        a = sin(dlat/2)**2 + cos(from_vertice_lat) * cos(to_vertice_lat) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 * 1000
        return c * r

    def aStarPath(self, from_vertice, to_vertice):
        vertice_count = len(self.__vertices)
        closedList = [False for i in range(vertice_count)]
        openList = []
        verticeParam = [[-1, 0.0, 0.0, 0.0] for i in range(vertice_count)]

        openList.append([0.0, from_vertice])
        minIdx = 0
        while openList:
            current = openList.pop(minIdx)
            closedList[current[1]] = True

            for branch in range(vertice_count):
                if (self.adj_matrix[branch][current[1]] != 0) and (not closedList[branch]):
                    gNew = verticeParam[current[1]][2] + self.adj_matrix[branch][current[1]]

                    latBranch = self.getVerticeByIndex(branch).getLat()
                    longBranch = self.getVerticeByIndex(branch).getLong()
                    latToVer = self.getVerticeByIndex(to_vertice).getLat()
                    longToVer = self.getVerticeByIndex(to_vertice).getLong()
                    hNew = haversine(latBranch, longBranch, latToVer, longToVer)

                    fNew = gNew + hNew
                    if (verticeParam[branch][1] == -1 or verticeParam[branch][1] > fNew):
                        openList.append(fNew, branch)
                        verticeParam[branch][0] = current[1]
                        verticeParam[branch][1] = fNew
                        verticeParam[branch][2] = gNew
                        verticeParam[branch][3] = hNew

            min = openList[0][0]
            for i in len(openList):
                if openList[i][0] < min:
                    minIdx = i

            branch = openList[minIdx][1]
            if branch == to_vertice:
                verticeParam[branch][0] = current[1]
                return self.getPath(verticeParam, to_vertice)
        return None

        # path = ["Dalem Kaum", "Alun-Alun Timur", "Balonggede A", "Balonggede B", "Balonggede C", "Balonggede D", "Dewi Sartika A"]
        # return path

    def getPath(self, verticeParam, to_vertice):
        path = [self.getVerticeByIndex(to_vertice).getName()]
        pred = verticeParam[to_vertice][0]
        print("pred = ", pred)
        while (pred != -1):
            path.append(self.getVerticeByIndex(pred).getName())
            pred = verticeParam[pred][0]
            print("pred = ", pred)
        return path

    def getPathMatrix(self, path):
        vertice_count = len(self.__vertices)
        path_matrix = [[0 for i in range(vertice_count)] for j in range(vertice_count)]
        for i in range(len(path) - 1):
            from_idx = self.getVerticeIndex(path[i])
            dest_idx = self.getVerticeIndex(path[i + 1])
            path_matrix[from_idx][dest_idx] = 1
            path_matrix[dest_idx][from_idx] = 1
        return path_matrix

    def getPathDistance(self, path):
        distance = 0
        for i in range(len(path) - 1):
            from_idx = self.getVerticeIndex(path[i])
            dest_idx = self.getVerticeIndex(path[i + 1])
            distance += self.__adj_matrix[from_idx][dest_idx]
        return distance

    def showVerticesName(self):
        for i in range(len(self.__vertices)):
            print(str(i + 1) + ". " + self.__vertices[i].getName())
            

# graph = Graph("../test/Sekitar_ITB.txt")
# vertices = graph.getVertices()
# param = [[-1], [0], [1]]
# path = graph.getPath(param, 2)
# print("Jalur yang ditemukan: " + path[0], end = "")
# for i in range(1, len(path)):
#     print(" --> " + path[i], end = "")
# print("")

# for i in range(len(vertices)):
#     print(vertices[i])
#     print(vertices[i].getName())
#     print(vertices[i].getCoordinate().getLat())
#     print(vertices[i].getCoordinate().getLong())
#     print(vertices[i].getParent())
#     print(vertices[i].getFn())
# print(graph.getAdjMatrix())

# print(graph.euclideanDistance(0, 0, 3, 4))
# print(graph.haversine(-6.890968379818, 107.61064263724266, -6.878229213627043, 107.60935517694757)) # Jarak asrama ke itb
