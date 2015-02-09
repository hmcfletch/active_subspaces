from unittest import TestCase
import unittest
import active_subspaces.gaussquad as gq
import numpy as np

class TestGaussquad(TestCase):
    def test_r_hermite_type_error(self):
        self.assertRaises(TypeError, gq.r_hermite, 'string')

    def test_r_hermite_0(self):
        self.assertRaises(ValueError, gq.r_hermite, 0)

    def test_r_hermite_1(self):
        v = gq.r_hermite(1)
        self.assertIsInstance(v, np.ndarray)
        np.testing.assert_equal(v, np.array([[0.0, 1.0]]))

    def test_r_hermite_2(self):
        v = gq.r_hermite(2)
        self.assertIsInstance(v, np.ndarray)
        np.testing.assert_equal(v, np.array([[0.0, 1.0], [0.0, 0.5], [0.0, 1.0]]))

    def test_r_hermite_5(self):
        v = gq.r_hermite(5)
        self.assertIsInstance(v, np.ndarray)
        np.testing.assert_equal(v, np.array([[0.0, 1.0], [0.0, 0.5], [0.0, 1.0], [0.0, 1.5], [0.0, 2.0], [0.0, 2.5]]))

    def test_jacobi_matrix_type_error(self):
        self.assertRaises(TypeError, gq.jacobi_matrix, 'string')

    def test_jacobi_matrix_multi_dimension_1(self):
        self.assertRaises(ValueError, gq.jacobi_matrix, np.array([0.0]))

    def test_jacobi_matrix_multi_dimension_2(self):
        self.assertRaises(ValueError, gq.jacobi_matrix, np.array([[[0.0, 1.0], [0.1, 2.0]],[[0.0, 1.0], [0.1, 2.0]]]))

    def test_jacobi_matrix_multi_dimension_num_columns_1(self):
        self.assertRaises(ValueError, gq.jacobi_matrix, np.array([[0.0], [0.1]]))

    def test_jacobi_matrix_multi_dimension_num_columns_2(self):
        self.assertRaises(ValueError, gq.jacobi_matrix, np.array([[0.0, 2.4, 5.2], [0.1, 21.5, 0.3]]))

    def test_jacobi_matrix_one_row_1(self):
        a = np.array([[0.0, 1.0]])
        np.testing.assert_equal(gq.jacobi_matrix(a), 0.0)

    def test_jacobi_matrix_one_row_2(self):
        a = np.array([[2.0, 1.0]])
        np.testing.assert_equal(gq.jacobi_matrix(a), 2.0)

    def test_jacobi_matrix_5(self):
        data = np.load('active_subspaces/tests/data/test_jacobi_matrix_5.npz')
        J = data['J']
        np.testing.assert_equal(gq.jacobi_matrix(gq.r_hermite(5)), J)

    def test_gh1d_7pts(self):
        data = np.load('test_gh1d_7pts.npz')
        p,w = gq.gh1d(7)
        np.testing.assert_equal(p, data['p'])
        np.testing.assert_equal(w, data['w'])

    def test_gauss_hermite_1d_array_arg(self):
        data = np.load('test_gh1d_7pts.npz')
        p,w = gq.gauss_hermite([7])
        np.testing.assert_equal(p, data['p'])
        np.testing.assert_equal(w, data['w'])

    def test_gauss_hermite_1d_int_arg(self):
        data = np.load('test_gh1d_7pts.npz')
        p,w = gq.gauss_hermite(7)
        np.testing.assert_equal(p, data['p'])
        np.testing.assert_equal(w, data['w'])

    def test_gauss_hermite_2d(self):
        data = np.load('test_gauss_hermite_2d.npz')
        p,w = gq.gauss_hermite([4,3])
        np.testing.assert_equal(p, data['p'])
        np.testing.assert_equal(w, data['w'])

    def test_gauss_hermite_3d(self):
        data = np.load('test_gauss_hermite_3d.npz')
        p,w = gq.gauss_hermite([5,6,7])
        np.testing.assert_equal(p, data['p'])
        np.testing.assert_equal(w, data['w'])

    def test_gauss_hermite_type_error(self):
        self.assertRaises(TypeError, gq.gauss_hermite, 'sting')

    @unittest.skip('not implemented yet')
    def test_gh1d(self):
        self.fail('not implemented yet')

    @unittest.skip('not implemented yet')
    def test_gauss_hermite(self):
        self.fail('not implemented yet')
