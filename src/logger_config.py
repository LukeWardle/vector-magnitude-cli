import logging
import os
from datetime import datetime

def setup_logger(name: str = 'vector_cli'):
  """
  Configure logging for the application.
  
  """

  # Create logs directory
  os.makedirs('logs', exist_ok=True)

  # Create logger
  logger = logging.getLogger(name)
  logger.setLevel(logging.INFO)

  # Clear existing handlers
  logger.handlers = []

  # Console handler
  console_handler = logging.StreamHandler()
  console_handler.setLevel(logging.INFO)
  console_format = logging.Formatter('%(message)s')
  console_handler.setFormatter(console_format)

  # File handler
  timestamp = datetime.now().strftime('%y%m%d_%H%M%S')
  file_handler = logging.FileHandler(f'logs/vector_cli_{timestamp}.log')
  file_handler.setLevel(logging.DEBUG)
  file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  file_handler.setFormatter(file_format)

  # Add handler
  logger.addHandler(console_handler)
  logger.addHandler(file_handler)

  return logger