import numpy as np
import numpy.ma as ma
import copy
class Map:
    vertices = []
    width = None
    height = None
    matrix = {}

    def __init__(self,width: int, height: int):
        self.width = width
        self.height = height
        self.matrix['map'] = [[0 for i in range(height)] for j in range(width)]


    def set_matrix(self, matrix):
        self.matrix['map'] = matrix

    def set_shape_matrix(self, matrix):
        self.matrix['shape'] = matrix

    def set_elevation_matrix(self, matrix):
        self.matrix['elevation'] = matrix


    def elaborate(self):
        shape_matrix = self.matrix['shape']

        elevation_matrix = self.matrix['elevation']

        result = ma.array(elevation_matrix, mask=shape_matrix)
        self.set_matrix(result)

    def print(self):
        print("Width: ", self.width)
        print("Height: ", self.height)
        for key, matrix in self.matrix.items():
           print(key, matrix)
