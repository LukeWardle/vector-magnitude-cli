"""
Command-line interface for vector magnitude calculations.

This script provides a user-friendly CLI for computing vector magnitudes.

"""

import argparse
import sys
from src.vector_utils import vector_magnitude

__version__ = "1.0.0"

def parse_arguments():
  """
  Parse command-line arguments.

  Returns:
    Namespace object containing parsed arguments.

  """

  parser = argparse.ArgumentParser(
    description="Calculate the Euclidean magnitude of a vector.",
    epilog="Example: python main.py --vector \"3, 4, 5\""
  )

  parser.add_argument(
    "--vector",
    type=str,
    required=False,
    help="Comma-seperated vector components (e.g., '3, 4, 5')"
  )

  parser.add_argument(
    "--verbose",
    action="store_true",
    help="Show detailed calculation steps"
  )

  parser.add_argument(
    "--version",
    action="version",
    version=f"%(prog)s {__version__}"
  )

  parser.add_argument(
    "--file",
    type=str,
    help="Path to file containing comma-separated vector"
  )

  return parser.parse_args()

def parse_vector_input(vector_string: str) -> list:
  """
  Parse a comma-seperated string into a list of floats.

  Args:
    vector_string: Comma-seperated numeric values.

  Returns:
    List of float values.
  
  Raises:
    ValueError: If input contains non-numeric values.
  
  """

  try:
    # Split by commas and convert each to float
    components = [float(x.strip()) for x in vector_string.split(',')]

    if not components:
      raise ValueError("Vector cannot be empty")
    
    return components
  
  except ValueError as e:
    raise ValueError(f"Invalid vector format: {e}")
  
def main():
  """
  Main execution function
  
  """

  try:

    # Parse command-line arguments
    args = parse_arguments()

    # Determine input source
    if args.file:
      try:
        with open(args.file, 'r') as f:
          vector_string = f.read().strip()
      except FileNotFoundError:
        print(f"Error: File '{args.file}' not found", file=sys.stderr)
        return 1
    elif args.vector:
      vector_string = args.vector
    else:
      print("Error: Provide either --vector or --file", file=sys.stderr)
      return 1

    # Parse vector from string input
    vector = parse_vector_input(vector_string)

    # Show verbose output if requested
    if args.verbose:
      print(f"Input vector: {vector}")
      print(f"Dimensions: {len(vector)}")
      print(f"Calculating: sqrt({' + '.join([f'{x}²' for x in vector])})")
      print()

    # Calculate magnitude
    magnitude = vector_magnitude(vector)

    # Display result
    print(f"Magnitude: {magnitude:.6f}")

    return 0 # Success
  
  except (ValueError, TypeError) as e:
    print(f"Error: {e}", file=sys.stderr)
    print("Try: python main.py --vector \"3, 4, 5\"", file=sys.stderr)
    return 1 # Error
  
  except KeyboardInterrupt:
    print("\nOperation cancelled by user.", file=sys.stderr)
    return 130 # Standard exit code for Ctrl+C
  

if __name__  == "__main__":
  sys.exit(main())