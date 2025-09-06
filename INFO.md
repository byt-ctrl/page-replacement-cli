# Project Documentation: Page Replacement Algorithm Solver

This document provides comprehensive technical documentation for each component of the Page Replacement Algorithm Solver project. It details the role, functionality, and interactions of every file in the implementation.

## Project Structure Overview

```
page-replacement-cli/
├── src/
│   ├── main.py           # Main application entry point
│   ├── fifo.py           # FIFO algorithm implementation
│   ├── lru.py            # LRU algorithm implementation
│   ├── optimal.py        # Optimal algorithm implementation
│   └── utils.py          # Utility functions and classes
├── requirements.txt  # Dependencies (none required)
├── README.md         # User documentation
└── INFO.md          # Technical documentation (this file)
```

## File-by-File Analysis

### main.py - Application Entry Point

**Role**: Serves as the main controller and user interface for the entire application. Handles user input, orchestrates algorithm execution, and manages the application flow.

**Key Components**:

#### Core Functions:

1. **`get_reference_string() -> List[int]`**
   - **Purpose**: Collects and validates the page reference sequence from user input
   - **Functionality**:
     - Prompts user for space-separated integers
     - Validates input format and content
     - Handles empty inputs and non-integer values
     - Supports keyboard interrupt for graceful exit
   - **Error Handling**: Comprehensive validation with user-friendly error messages

2. **`get_number_of_frames() -> int`**
   - **Purpose**: Obtains and validates the memory frame count
   - **Functionality**:
     - Accepts integer input for frame count
     - Validates positive integers
     - Warns about large frame counts (>50) that may affect display
     - Allows user to continue or retry
   - **Range**: Accepts 1-50+ frames with readability warnings

3. **`get_algorithm_choice() -> str`**
   - **Purpose**: Presents algorithm selection menu and captures user choice
   - **Functionality**:
     - Displays numbered menu options (1-5)
     - Options: FIFO, LRU, Optimal, Compare All, Help
     - Validates input against allowed choices
   - **Integration**: Returns choice string for algorithm routing

4. **`show_help()`**
   - **Purpose**: Provides detailed explanations of each algorithm
   - **Functionality**:
     - Clears screen for clean display
     - Explains FIFO, LRU, and Optimal algorithms
     - Includes advantages, disadvantages, and use cases
     - Pauses for user reading
   - **Educational Value**: Serves as built-in documentation

5. **`run_single_algorithm(choice: str, reference_string: List[int], frames: int) -> None`**
   - **Purpose**: Executes a single page replacement algorithm
   - **Functionality**:
     - Maps choice to algorithm class (FIFO, LRU, Optimal)
     - Instantiates algorithm with frame count
     - Runs simulation and displays results
     - Shows summary statistics (faults, ratio, etc.)
   - **Output**: Detailed results with colored formatting

6. **`run_comparison(reference_string: List[int], frames: int) -> None`**
   - **Purpose**: Compares all three algorithms side-by-side
   - **Functionality**:
     - Executes all algorithms sequentially
     - Collects performance metrics
     - Displays comparative table
     - Identifies best-performing algorithm
   - **Analysis**: Shows efficiency percentages relative to optimal

7. **`run_algorithm(choice: str, reference_string: List[int], frames: int) -> None`**
   - **Purpose**: Router function for algorithm execution
   - **Functionality**:
     - Directs flow based on user choice
     - Handles comparison mode (choice '4')
     - Manages help display (choice '5')
     - Routes single algorithms to appropriate handlers

8. **`get_continue_choice() -> str`**
   - **Purpose**: Manages post-execution user options
   - **Functionality**:
     - Offers: Run again, Change settings, Exit
     - Validates user selection
     - Enables workflow continuity
   - **State Management**: Allows resetting reference string or frame count

9. **`main()`**
   - **Purpose**: Main application loop and state management
   - **Functionality**:
     - Initializes application with welcome screen
     - Manages reference string and frame state
     - Handles algorithm selection and execution
     - Processes continuation choices
     - Provides graceful exit handling
   - **Exception Handling**: Catches KeyboardInterrupt and general exceptions

**Interactions**:
- **Imports**: Algorithm classes from src/fifo.py, src/lru.py, src/optimal.py; utilities from src/utils.py
- **Dependencies**: Relies on algorithm implementations for simulation logic
- **Output**: Uses src/utils.py functions for colored, formatted display

---

### fifo.py - FIFO Algorithm Implementation

**Role**: Implements the First-In-First-Out page replacement algorithm with step-by-step visualization.

**Key Components**:

#### FIFO Class:

1. **`__init__(self, frames: int)`**
   - **Purpose**: Initializes FIFO algorithm state
   - **Attributes**:
     - `frames`: Number of memory frames
     - `page_queue`: List maintaining page order (queue)
     - `page_set`: Set for O(1) page lookup
     - `page_faults`: Counter for page faults

2. **`print_step(self, reference: int, current_index: int, total_references: int, is_fault: bool) -> None`**
   - **Purpose**: Displays current simulation step with visual formatting
   - **Functionality**:
     - Shows step counter, current page, memory state
     - Uses colored output for FAULT/HIT status
     - Displays frame contents with empty slots
   - **Visualization**: Provides real-time memory state representation

3. **`load_page(self, page: int) -> bool`**
   - **Purpose**: Handles page loading logic for FIFO algorithm
   - **Functionality**:
     - Checks if page is already in memory (hit)
     - If fault: removes oldest page if frames full, adds new page
     - Updates queue and set accordingly
     - Increments fault counter
   - **Algorithm Logic**: Pure FIFO replacement when frames are full

4. **`run(self, reference_string: List[int]) -> int`**
   - **Purpose**: Executes complete FIFO simulation
   - **Functionality**:
     - Resets algorithm state
     - Processes each page in reference string
     - Calls print_step for each reference
     - Returns total page faults
   - **Return Value**: Integer count of page faults

**Interactions**:
- **Dependencies**: Uses `Colors` and `print_algorithm_header` from utils.py
- **Integration**: Implements standard interface (run method) for main.py
- **Data Structures**: Uses list for queue, set for fast lookup

---

### lru.py - LRU Algorithm Implementation

**Role**: Implements the Least Recently Used page replacement algorithm with access tracking.

**Key Components**:

#### LRU Class:

1. **`__init__(self, frames: int)`**
   - **Purpose**: Initializes LRU algorithm state
   - **Attributes**:
     - `frames`: Number of memory frames
     - `page_list`: List maintaining access order (MRU to LRU)
     - `page_set`: Set for O(1) page lookup
     - `page_faults`: Counter for page faults

2. **`print_step(self, reference: int, current_index: int, total_references: int, is_fault: bool) -> None`**
   - **Purpose**: Displays current simulation step
   - **Functionality**: Identical to FIFO's print_step method
   - **Visualization**: Consistent formatting across algorithms

3. **`load_page(self, page: int) -> bool`**
   - **Purpose**: Handles page loading with LRU replacement logic
   - **Functionality**:
     - Checks for page hit
     - On hit: moves page to end (most recently used)
     - On fault: removes LRU page if frames full, adds new page
     - Updates list and set
   - **Algorithm Logic**: Maintains recency order, replaces least recent

4. **`run(self, reference_string: List[int]) -> int`**
   - **Purpose**: Executes complete LRU simulation
   - **Functionality**: Similar to FIFO's run method
   - **State Management**: Resets all attributes before simulation

**Interactions**:
- **Dependencies**: Uses utils.py for display functions
- **Integration**: Same interface as other algorithms
- **Data Structures**: List for order maintenance, set for lookup

---

### optimal.py - Optimal Algorithm Implementation

**Role**: Implements the theoretically optimal page replacement algorithm using future knowledge.

**Key Components**:

#### Optimal Class:

1. **`__init__(self, frames: int)`**
   - **Purpose**: Initializes Optimal algorithm state
   - **Attributes**: Similar to LRU (page_list, page_set, page_faults)

2. **`print_step(self, reference: int, current_index: int, total_references: int, is_fault: bool, victim_page: int = None) -> None`**
   - **Purpose**: Enhanced step display showing replaced page
   - **Functionality**:
     - Includes victim page information when replacement occurs
     - Shows which page was replaced for educational value

3. **`find_farthest_page(self, reference_string: List[int], current_index: int) -> int`**
   - **Purpose**: Determines which page to replace based on future usage
   - **Functionality**:
     - Scans future references for each page in memory
     - Finds page with farthest next usage
     - Handles pages not used again (infinite future distance)
   - **Algorithm Logic**: Core of optimal replacement strategy

4. **`load_page(self, page: int, reference_string: List[int], current_index: int) -> Tuple[bool, int]`**
   - **Purpose**: Handles page loading with optimal replacement
   - **Functionality**:
     - Checks for hit
     - On fault: finds optimal victim, replaces it
     - Returns fault status and victim page for display
   - **Return Value**: Tuple of (is_fault, victim_page)

5. **`run(self, reference_string: List[int]) -> int`**
   - **Purpose**: Executes optimal simulation
   - **Functionality**: Processes reference string with future knowledge

**Interactions**:
- **Dependencies**: Uses utils.py display functions
- **Integration**: Same interface pattern as other algorithms
- **Complexity**: O(n²) due to future scanning for each replacement

---

### utils.py - Utility Functions and Classes

**Role**: Provides shared utilities, constants, and helper functions used across the application.

**Key Components**:

#### Colors Class:
- **Purpose**: ANSI color codes for terminal output
- **Constants**: RESET, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, WHITE, BOLD, UNDERLINE
- **Usage**: Enables colored, formatted terminal output throughout the application

#### Display Functions:

1. **`clear_screen()`**
   - **Purpose**: Clears terminal screen for clean interface
   - **Implementation**: Uses `os.system('cls' if os.name == 'nt' else 'clear')`

2. **`print_header(text: str)`**
   - **Purpose**: Displays formatted section headers
   - **Formatting**: Centered text with border lines

3. **`print_algorithm_header(text: str)`**
   - **Purpose**: Algorithm-specific headers
   - **Styling**: Purple borders with blue centered text

4. **`print_success(text: str)`, `print_error(text: str)`, `print_warning(text: str)`, `print_info(text: str)`**
   - **Purpose**: Status message display with appropriate colors and icons
   - **Icons**: ✓ for success, ✗ for error, ⚠ for warning, ℹ for info

#### Utility Functions:

5. **`get_terminal_size()`**
   - **Purpose**: Gets current terminal dimensions
   - **Fallback**: Returns 80x24 if detection fails

6. **`validate_reference_string(ref_string: List[int]) -> bool`**
   - **Purpose**: Validates reference string format
   - **Checks**: Non-empty, all integers

7. **`validate_frames(frames: int) -> bool`**
   - **Purpose**: Validates frame count
   - **Checks**: Positive integer

8. **`format_output(...)`**
   - **Purpose**: Formats results for display
   - **Output**: Multi-line formatted string with colors

9. **`pause_execution()`**
   - **Purpose**: Pauses execution for user reading

10. **`confirm_exit()`**
    - **Purpose**: Confirms application exit

11. **`save_results_to_file(results: str, filename: str = None) -> bool`**
    - **Purpose**: Saves simulation results to file
    - **Features**: Auto-generates timestamped filename

12. **`load_reference_string_from_file(filename: str) -> List[int]`**
    - **Purpose**: Loads reference string from file

13. **`generate_sample_reference_string(length: int = 20, max_page: int = 10) -> List[int]`**
    - **Purpose**: Generates random reference string for testing

14. **`print_statistics(...)`**
    - **Purpose**: Displays detailed performance statistics
    - **Metrics**: Hits, faults, ratios, frame usage

**Interactions**:
- **Usage**: Imported by all other modules for display and utility functions
- **Central Role**: Provides consistent formatting and shared functionality
- **Extensibility**: Additional utilities can be added here

---

### requirements.txt - Dependencies

**Role**: Specifies project dependencies (minimal for this project).

**Content**:
```
# No external dependencies required - using only standard Python libraries
```

**Explanation**:
- **Philosophy**: Uses only Python standard library modules
- **Benefits**: No installation requirements, maximum portability
- **Modules Used**: `sys`, `time`, `os`, `typing` (all standard)

---

## Component Interactions

### Data Flow:
1. **src/main.py** collects user input (reference string, frames)
2. **src/main.py** instantiates chosen algorithm class
3. **Algorithm classes** (src/fifo.py, src/lru.py, src/optimal.py) execute simulation
4. **Algorithm classes** use **src/utils.py** for display formatting
5. **src/main.py** displays results and handles continuation

### Interface Consistency:
- All algorithm classes implement the same interface:
  - `__init__(frames: int)`
  - `run(reference_string: List[int]) -> int`
- Enables polymorphic usage in src/main.py

### Shared Resources:
- **Colors** class provides consistent color scheme
- **Display functions** ensure uniform output formatting
- **Validation functions** standardize input checking

### Error Handling:
- **src/main.py**: Handles user input validation and exceptions
- **Algorithm classes**: Focus on algorithm logic
- **src/utils.py**: Provides error display functions

---

## Key Design Patterns

### Strategy Pattern:
- Algorithm classes implement interchangeable strategies
- src/main.py selects and executes appropriate algorithm
- Enables easy addition of new algorithms

### Template Method Pattern:
- All algorithms follow same simulation structure
- `run()` method provides consistent execution flow
- Individual `load_page()` methods implement specific logic

### Utility Class Pattern:
- src/utils.py serves as centralized utility provider
- Static methods for common operations
- No instantiation required

---

## Performance Characteristics

### Time Complexity:
- **FIFO/LRU**: O(n) where n is reference string length
- **Optimal**: O(n²) due to future scanning
- **Comparison Mode**: O(n²) (dominated by Optimal)

### Space Complexity:
- **All Algorithms**: O(f) where f is frame count
- **Optimal**: Additional O(n) for future reference scanning

### Practical Considerations:
- Optimal algorithm is theoretical (requires future knowledge)
- FIFO/LRU suitable for real-world implementation
- Comparison mode useful for educational purposes

---

## Extensibility

### Adding New Algorithms:
1. Create new class inheriting from base pattern
2. Implement `__init__` and `run` methods
3. Add to algorithm mappings in src/main.py
4. Update help text and menus

### Enhancing Features:
- Add new utilities to src/utils.py
- Extend statistics in print_statistics()
- Add file I/O capabilities
- Implement GUI interface

---

## Known Limitations

1. **Optimal Algorithm**: Requires complete reference string (not practical)
2. **Display Width**: Large frame counts may exceed terminal width
3. **Memory Usage**: Optimal algorithm scans future references repeatedly
4. **Input Size**: No upper limit on reference string length

---

## Educational Value

This implementation serves as:
- **Algorithm Demonstration**: Clear visualization of replacement strategies
- **Performance Comparison**: Quantitative analysis of algorithm efficiency
- **Code Example**: Well-structured Python implementation
- **Learning Tool**: Interactive exploration of OS concepts

---