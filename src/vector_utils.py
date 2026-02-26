"""
Vector utility functions for mathematical operations.

This module provides core vector operations including magnitude calculation using
the Euclidean norm (L2 norm).

"""

import numpy as np
import matplotlib.pyplot as plt
import os
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
  if vector is None or len(vector) == 0:
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

def visualise_2d_vector(vector: list, output_path: str = 'outputs/vector_plot.png'):
  """
  Create a 2D visualisation of a vector.

  Args:
    vector: A 2D vector [x, y]
    output_path: Where to save the plot

  Raises:
    ValueError: If vector is not 2D
  
  """

  if len(vector) != 2:
    raise ValueError("Vector must be 2D for visualisation")
  
  # Ensure output directory exists
  os.makedirs(os.path.dirname(output_path), exist_ok=True)

  # Create figure
  fig, ax = plt.subplots(figsize=(8, 8))

  # Draw vector as arrow from origin
  ax.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='blue', width=0.006)

  # Set axis limits with some padding
  max_val = max(abs(vector[0]), abs(vector[1])) * 1.2
  ax.set_xlim(-max_val, max_val)
  ax.set_ylim(-max_val, max_val)

  # Add grid and labels
  ax.grid(True, alpha=0.3)
  ax.axhline(y=0, color='k', linewidth=0.5)
  ax.axvline(x=0, color='k', linewidth=0.5)
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_title(f'Vector [{vector[0]}, {vector[1]}]\nMagnitude: {vector_magnitude(vector):.3f}')
  ax.set_aspect('equal')

  # Save
  plt.tight_layout()
  plt.savefig(output_path, dpi=150, bbox_inches='tight')
  plt.close()
