"""
Unit tests for vector_utils module.

"""

import pytest
import numpy as np
from src.vector_utils import vector_magnitude

def test_magnitude_3_4_5_triangle():
  """
  Test with classic 3-4-5 right triangle.
  
  """
  assert vector_magnitude([3, 4]) == pytest.approx(5.0)

def test_magnitude_3d_vector():
  """
  Test with 3D vector [2, 2, 1] -> magnitude 3.
  
  """
  assert vector_magnitude([2, 2, 1]) == pytest.approx(3.0)

def test_magnitude_unit_vectors():
  """
  Test unit vectors in different dimensions.
  
  """
  assert vector_magnitude([1, 0]) == pytest.approx(1.0)
  assert vector_magnitude([0, 1, 0]) == pytest.approx(1.0)
  assert vector_magnitude([0, 0, 0, 1]) == pytest.approx(1.0)

def test_magnitude_zero_vector():
  """
  Test zero vector has magnitude 0.

  """
  assert vector_magnitude([0, 0, 0]) == pytest.approx(0.0)

def test_magnitude_high_dimensional():
  """
  Test with high-dimensional vector

  """
  # All ones vector of length 10: sqrt(10) ≈ 3.162
  vector = [1] * 10
  assert vector_magnitude(vector) == pytest.approx(np.sqrt(10))

def test_magnitude_negative_components():
  """
  Test that negative components work correctly.
  
  """
  # [-3, 4] should also give magnitude 5
  assert vector_magnitude([-3, 4]) == pytest.approx(5.0)
  assert vector_magnitude([-3, -4]) == pytest.approx(5.0)

def test_magnitude_empty_vector_raises():
  """
  Test that empty vector raises ValueError.
  
  """
  with pytest.raises(ValueError, match="Vector cannot be empty"): vector_magnitude([])

def test_magntiude_non_numeric_raises():
  """
  Test that non-numeric input raises TypeError.
  
  """
  with pytest.raises(TypeError, match="numeric values"):
    vector_magnitude(['a', 'b', 'c'])

def test_magnitude_numpy_array_input():
  """
  Test that NumPy arrays work as input.
  
  """
  arr = np.array([3, 4])
  assert vector_magnitude(arr) == pytest.approx(5.0)