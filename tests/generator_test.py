from unittest import TestCase
from src.tasselator import VoronoiTasselator
import numpy as np

class GeneratorTest(TestCase):


    def test_true(self):
        self.assertTrue(True)

    def test_if_generator_make_from_points_does_not_receive_dimension_exception_should_be_raised(self):
        self.assertRaises(Exception, VoronoiTasselator.make_from_points, (), np.random.rand(10, 2))

    def test_if_generator_make_from_points_does_not_receive_points_exception_should_be_raised(self):
        points = np.random.rand(0, 2)
        self.assertRaises(Exception, VoronoiTasselator.make_from_points, (10, 10), points)

    def test_generate_map_should_return_a_voronoi_object(self):
        pass

    def test_relax_diagram_should_accept_number_of_iterations(self):
        pass

    def test_relax_diagram_should_retunr_a_voronoi_object(self):
        pass