# Note:
# __init__ di objek itu konstruktor
# '__' di depan variabel itu artinya private (khusus python)
# 'self' itu mirip dengan 'this'
# Kalau mau copy object, pakai deepcopy
# Coba cek 'a star algorithm' di geekforgeeks

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
    __parent = None # String
    __fn = None # Float
    __gn = None # Float

    # Public
    def __init__(self, name, lat, long, parent, fn, gn):
        self.__name = name
        self.__coordinate = Coordinate(lat, long)
        self.__parent = parent
        self.__fn = fn
        self.__gn = gn

    def getName(self):
        return self.__name

    def getCoordinate(self):
        return self.__coordinate

    def getParent(self):
        return self.__parent

    def getFn(self):
        return self.__fn

    def getGn(self):
        return self.__gn

    def setName(self, name):
        self.__name = name

    def setCoordinate(self, lat, long):
        self.__coordinate = Coordinate(lat, long)

    def setParent(self, parent):
        self.__parent = parent

    def setFn(self, fn):
        self.__fn = fn

    def setGn(self, gn):
        self.__gn = gn

    def resetVertice(self):
        self.__parent = ""
        self.__gn = 0

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
            
            self.__vertices.append(Vertice(vertice_name, vertice_lat, vertice_long, "", 0, 0))

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
        path = []
        return path

graph = Graph("../test/test.txt")
vertices = graph.getVertices()
for i in range(len(vertices)):
    print(vertices[i])
    print(vertices[i].getName())
    print(vertices[i].getCoordinate().getLat())
    print(vertices[i].getCoordinate().getLong())
    print(vertices[i].getParent())
    print(vertices[i].getFn())
print(graph.getAdjMatrix())

print(graph.euclideanDistance(0, 0, 3, 4))
print(graph.haversine(-6.890968379818, 107.61064263724266, -6.878229213627043, 107.60935517694757)) # Jarak asrama ke itb