# Page Replacement Algorithm Solver

A comprehensive command-line tool for simulating and comparing page replacement algorithms used in operating systems memory management. This educational tool demonstrates FIFO (First-In-First-Out), LRU (Least Recently Used), and Optimal page replacement algorithms with interactive visualization and detailed statistics.

## Purpose

This project serves as an educational tool to help students and developers understand how different page replacement algorithms work in operating systems. By providing step-by-step simulation and comparison features, users can visualize the behavior of each algorithm and analyze their performance metrics.

## Key Features

- **Interactive CLI Interface**: User-friendly command-line interface with colored output
- **Three Algorithm Implementations**:
  - FIFO (First-In-First-Out)
  - LRU (Least Recently Used)
  - Optimal (Theoretical benchmark)
- **Step-by-Step Visualization**: Real-time display of page faults, hits, and memory state
- **Algorithm Comparison**: Side-by-side performance comparison of all algorithms
- **Input Validation**: Robust error handling and user input validation
- **Detailed Statistics**: Page fault ratios, hit rates, and efficiency metrics
- **Flexible Configuration**: Customizable reference strings and frame counts
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Prerequisites

- **Python Version**: Python 3.6 or higher
- **Operating System**: Windows, macOS, or Linux
- **Terminal**: Any modern terminal that supports ANSI color codes

## Installation

### Option 1: Direct Download
1. Download all project files to your local machine
2. Ensure Python 3.6+ is installed on your system

### Option 2: Clone Repository (if applicable)
```bash
git clone <repository-url>
cd page-replacement-cli
```

### Dependencies
This project uses only standard Python libraries - no external dependencies required!

## Usage

### Running the Application
```bash
python main.py
```

### Basic Workflow
1. **Enter Reference String**: Provide a sequence of page references (space-separated integers)
   - Example: `1 2 3 4 1 2 5 1 2 3 4 5`

2. **Specify Frame Count**: Enter the number of memory frames (1-20 recommended)

3. **Choose Algorithm**:
   - **1**: Run FIFO algorithm
   - **2**: Run LRU algorithm
   - **3**: Run Optimal algorithm
   - **4**: Compare all algorithms
   - **5**: View help information

### Example Session
```
Page Replacement Algorithm Solver
============================================================
Enhanced Version with Colors and Advanced Features
============================================================

Enter the reference string (space-separated integers)
Example: 1 2 3 4 1 2 5 1 2 3 4 5
>>> 1 2 3 4 1 2 5 1 2 3 4 5

Enter the number of frames (1-20 recommended)
>>> 3

Choose the algorithm to run:
1. FIFO (First-In-First-Out)
2. LRU (Least Recently Used)
3. OPR/OPT (Optimal)
4. Compare All Algorithms
5. Help
Enter your choice (1-5): 4
```

## Algorithm Explanations

### FIFO (First-In-First-Out)
- **Principle**: Replaces the oldest page currently in memory
- **Advantages**: Simple to implement, low overhead
- **Disadvantages**: Can suffer from Belady's anomaly, suboptimal performance
- **Use Case**: Basic memory management scenarios

### LRU (Least Recently Used)
- **Principle**: Replaces the page that hasn't been accessed for the longest time
- **Advantages**: Better performance than FIFO, approximates optimal behavior
- **Disadvantages**: More complex implementation, requires tracking access times
- **Use Case**: Most common replacement strategy in modern operating systems

### Optimal (OPT)
- **Principle**: Replaces the page that will not be used for the longest time in the future
- **Advantages**: Theoretically optimal performance
- **Disadvantages**: Impossible to implement in practice (requires future knowledge)
- **Use Case**: Benchmark for comparing other algorithms

## Output Interpretation

### Step-by-Step Display
```
Step 1/12     | Page: 1    | Frames: [1] [ ] [ ] | Status: FAULT
Step 2/12     | Page: 2    | Frames: [1] [2] [ ] | Status: FAULT
```

- **Step**: Current position in reference string
- **Page**: Page being referenced
- **Frames**: Current state of memory frames
- **Status**: HIT (page found in memory) or FAULT (page loaded from disk)

### Summary Statistics
```
Algorithm: FIFO (First-In-First-Out)
Reference String: 1 2 3 4 1 2 5 1 2 3 4 5
Number of Frames: 3
Total Page Faults: 7
Total References: 12
Page Fault Ratio: 58.33%
```

## Algorithm Comparison

When choosing "Compare All Algorithms", the tool provides:
- Side-by-side performance metrics
- Efficiency ratings relative to the best algorithm
- Clear identification of the most effective algorithm for your reference string

## Advanced Features

- **Input Validation**: Handles invalid inputs gracefully with helpful error messages
- **Keyboard Interrupt Handling**: Clean exit on Ctrl+C
- **Screen Clearing**: Maintains clean interface between operations
- **Flexible Reference Strings**: Support for any integer sequence
- **Frame Limit Warnings**: Alerts for large frame counts that may affect readability

## Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup
```bash
# Ensure Python 3.6+ is installed
python --version

# Run the application
python main.py

# Test with sample data
# Reference string: 1 2 3 4 1 2 5 1 2 3 4 5
# Frames: 3
```

## License

This project is open source and available under the MIT License.