# Vector Magnitude CLI Tool


A command-line tool for calculating the Euclidean magnitude (L2 norm) of vectors. Built as part of Week 1 of an AI Engineering course, demonstrating professional Python development practices including modular design, comprehensive testing, and CLI interface design.


## 📋 Table of Contents


- [Features](#features)
- [Mathematical Background](#mathematical-background)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Development](#development)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [License](#license)
- [Contact](#contact)


## ✨ Features


- 🎯 **Accurate Calculations**: Implements Euclidean norm (L2 norm) using NumPy for numerical precision
- 🖥️ **Command-Line Interface**: Professional CLI with argparse for easy integration into workflows
- 📊 **Verbose Mode**: Shows detailed calculation steps for educational purposes
- 🛡️ **Robust Error Handling**: Graceful handling of invalid inputs with clear error messages
- ✅ **Comprehensive Testing**: 9 unit tests covering edge cases and normal operations
- 📖 **Well-Documented**: Google-style docstrings and type hints throughout
- 🔢 **Multi-Dimensional**: Works with vectors of any dimension (2D, 3D, or higher)


## 📐 Mathematical Background


The **Euclidean magnitude** (or L2 norm) of a vector **v** = [v₁, v₂, ..., vₙ] is defined as:


```
||v|| = √(v₁² + v₂² + ... + vₙ²)
```


This represents the straight-line distance from the origin to the point defined by the vector in n-dimensional space.


**Example**: For vector [3, 4]:
- ||[3, 4]|| = √(3² + 4²) = √(9 + 16) = √25 = 5


### Applications


- **Machine Learning**: Feature normalization, distance metrics, regularization
- **Computer Vision**: Image processing, optical flow
- **Data Science**: Similarity measures, clustering algorithms
- **Physics**: Velocity calculations, force vectors


## 🚀 Installation


### Prerequisites


- Python 3.8 or higher
- pip (Python package manager)


### Setup


1. **Clone the repository**


```bash
git clone https://github.com/LukeWardle/vector-magnitude-cli.git
cd vector-magnitude-cli
```


2. **Create and activate virtual environment**


```bash
# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate


# Windows
python -m venv .venv
.venv\Scripts\activate
```


3. **Install dependencies**


```bash
pip install -r requirements.txt
```


## 💻 Usage


### Basic Usage


```bash
python main.py --vector "3,4"
```


**Output:**
```
Magnitude: 5.000000
```


### Verbose Mode


Show detailed calculation steps:


```bash
python main.py --vector "2,2,1" --verbose
```


**Output:**
```
Input vector: [2.0, 2.0, 1.0]
Dimension: 3
Calculating: sqrt(2.0² + 2.0² + 1.0²)


Magnitude: 3.000000
```


### Getting Help


```bash
python main.py --help
```


## 📚 Examples


### 2D Vector (Classic 3-4-5 Triangle)


```bash
python main.py --vector "3,4"
# Output: Magnitude: 5.000000
```


### 3D Vector


```bash
python main.py --vector "1,2,2"
# Output: Magnitude: 3.000000
```


### High-Dimensional Vector


```bash
python main.py --vector "1,1,1,1,1,1,1,1,1,1"
# Output: Magnitude: 3.162278 (√10)
```


### Unit Vector


```bash
python main.py --vector "1,0,0"
# Output: Magnitude: 1.000000
```


## 🛠️ Development


### Running Tests


```bash
# Run all tests
pytest


# Run with verbose output
pytest -v


# Run specific test file
pytest tests/test_vector_utils.py


# Run with coverage report
pytest --cov=src tests/
```


### Code Quality


The codebase follows these standards:


- **PEP 8**: Python style guide compliance
- **Type Hints**: All functions have type annotations
- **Docstrings**: Google-style documentation for all public functions
- **Testing**: Comprehensive test coverage with pytest


## 📁 Project Structure


```
vector-magnitude-cli/
├── .venv/                 # Virtual environment (not in Git)
├── src/                   # Source code
│   ├── __init__.py       # Package initialization
│   └── vector_utils.py   # Core vector operations
├── tests/                 # Test suite
│   ├── __init__.py
│   └── test_vector_utils.py  # Unit tests
├── .gitignore            # Git ignore rules
├── main.py               # CLI entry point
├── README.md             # This file
└── requirements.txt      # Python dependencies
```


## 🔧 Technologies Used


- **Python 3.8+**: Core programming language
- **NumPy**: Efficient numerical computations
- **argparse**: Command-line interface
- **pytest**: Testing framework


## 📄 License


This project is licensed under the MIT License - see below for details:


```
MIT License


Copyright (c) 2026 Luke Wardle


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:


The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```


## 👤 Contact


**Luke Wardle**


- GitHub: [@Luke Wardle](https://github.com/LukeWardle)
- Email: l.wardle@live.co.uk


---


**Part of Week 1 - AI Engineering Course**


This project demonstrates professional Python development practices including:
- Modular code organization
- Comprehensive testing with pytest
- CLI interface design
- Professional documentation
- Version control with Git

