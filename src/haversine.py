from math import radians, cos, sin, asin, sqrt

''' Ini cuma biar gampang bikin testcase '''

def haversine(from_vertice_lat, from_vertice_long, to_vertice_lat, to_vertice_long):
        from_vertice_lat, from_vertice_long, to_vertice_lat, to_vertice_long = map(radians, [from_vertice_lat, from_vertice_long, to_vertice_lat, to_vertice_long])
        dlon = to_vertice_long - from_vertice_long
        dlat = to_vertice_lat - from_vertice_lat 
        a = sin(dlat/2)**2 + cos(from_vertice_lat) * cos(to_vertice_lat) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 * 1000
        return c * r

print(haversine(-6.896941653108604, 107.61053587810535, -6.898230446493914, 107.61034812347313))