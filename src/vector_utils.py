"""
Vector utility functions for mathematical operations.

This module provides core vector operations including magnitude calculation using
the Euclidean norm (L2 norm).

"""

import numpy as np
from typing import List, Union

def vector_magnitude(vector: Union[List[float], np.ndarray]) -> float:

  """
  Calculate the Euclidean magnitude (L2 norm) of a vector.

  The magnitude is the straight-line distance from the origin to the point represented by the vector in n-dimensional space.

  Formula: ||v|| = sqrt(v₁² + v₂² + ... + vₙ²)

  Args:
    vector: A list or NumPy array of numeric values representing the vector components. Can be any dimensions.

  Returns:
    The magnitude of the vector as a float.

  Raises:
    ValueError: If the input vector is empty.
    TypeError: If vector contains non-numeric values.

  Examples:
    >>> vector_magnitude([3, 4])
    5.0
    >>> vector_magnitude([1, 0, 0])
    1.0
    >>> vector_magnitude([2, 2, 1])
    3.0

  """

  # Validate input
  if not vector or len(vector) == 0:
    raise ValueError("Vector cannot be empty")
  
  # Convert to NumPy array for efficient vectorised computation
  try:
    np_vector = np.array(vector, dtype=float)
  except (ValueError, TypeError) as e:
    raise TypeError(f"Vector must contain only numeric values: {e}")
  
  # Calculate magnitude using vectorised NumPy operations
  # Formula: sqrt(sum of squared components)
  magnitude = np.sqrt(np.sum(np.square(np_vector)))
  return float(magnitude)