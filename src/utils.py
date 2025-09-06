# utility functions for Page Replacement Algorithm Solver

import os
import sys
import time
from typing import List

class Colors :
    # ANSI color codes for terminal output
    RESET='\033[0m'
    RED='\033[91m'
    GREEN='\033[92m'
    YELLOW='\033[93m'
    BLUE='\033[94m'
    PURPLE='\033[95m'
    CYAN='\033[96m'
    WHITE='\033[97m'
    BOLD='\033[1m'
    UNDERLINE='\033[4m'

# emojis that are use in this code are taken from online (for better visualisation)
def clear_screen() :
    # clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text : str) :
    # print a formatted header
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.WHITE}{text:^60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.RESET}")

def print_algorithm_header(text : str) :
    # print a formatted algorithm header
    print(f"{Colors.BOLD}{Colors.PURPLE}{'-' * 50}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text:^50}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.PURPLE}{'-' * 50}{Colors.RESET}")

def print_success(text : str) :
    # print success message
    print(f"{Colors.GREEN}{Colors.BOLD} ✓ {text}{Colors.RESET}")

def print_error(text : str):
    # print error message
    print(f"{Colors.RED}{Colors.BOLD} ✗ {text}{Colors.RESET}")

def print_warning(text : str):
    # print warning message
    print(f"{Colors.YELLOW}{Colors.BOLD} ⚠ {text}{Colors.RESET}")

def print_info(text : str) :
    # print info message
    print(f"{Colors.BLUE}ℹ {text}{Colors.RESET}")

def get_terminal_size() :
    # get terminal dimensions
    try :
        columns , rows=os.get_terminal_size()
        return columns , rows
    except :
        return 80 , 24

def validate_reference_string(ref_string : List[int]) -> bool :
    # validate the reference string
    if not ref_string :
        return False
    return all(isinstance(page , int) for page in ref_string)

def validate_frames(frames : int) -> bool :
    # validate's the number of frames
    return isinstance(frames , int) and frames > 0

def format_output(algorithm_name : str , reference_string : List[int] , frames : int , page_faults : int) -> str :
    # format's the output for display
    return f"""
{Colors.BOLD}{Colors.CYAN}Algorithm:{Colors.RESET} {algorithm_name}
{Colors.BOLD}{Colors.BLUE}Reference String:{Colors.RESET} {' '.join(map(str, reference_string))}
{Colors.BOLD}{Colors.YELLOW}Frames:{Colors.RESET} {frames}
{Colors.BOLD}{Colors.RED}Total Page Faults:{Colors.RESET} {page_faults}
"""

def pause_execution() :
    # pause's execution and wait for user input
    input(f"{Colors.YELLOW}Press Enter to continue......{Colors.RESET}")

def confirm_exit() :
    #confirm's exit with user
    try :
        response=input(f"{Colors.YELLOW}Are you sure you want to exit? (y/n) : {Colors.RESET}").strip().lower()
        return response in ['y', 'yes']
    except KeyboardInterrupt :
        return True

def save_results_to_file(results : str , filename : str = None) -> bool :
    # save's results to a file
    try :
        if filename is None :
            filename=f"page_replacement_results_{int(time.time())}.txt"
        
        with open(filename, 'w') as f :
            f.write(results)
        
        print_success(f"Results saved to {filename}")
        return True
    except Exception as e :
        print_error(f"Failed to save results : {e}")
        return False

def load_reference_string_from_file(filename : str) -> List[int] :
    # load's reference string from a file
    try :
        with open(filename , 'r') as f :
            content=f.read().strip()
            return list(map(int, content.split()))
    except Exception as e :
        print_error(f"Failed to load file : {e}")
        return []

def generate_sample_reference_string(length : int = 20 , max_page : int = 10) -> List[int] :
    # generate's a sample reference string for testing
    import random
    return [random.randint(0 , max_page) for _ in range(length)]

def print_statistics(reference_string : List[int] , frames : int , page_faults : int):
    # print detailed statistics
    total_references=len(reference_string)
    hit_count=total_references - page_faults
    hit_ratio=hit_count / total_references if total_references > 0 else 0
    fault_ratio=page_faults / total_references if total_references > 0 else 0
    
    print_header("Detailed Statistics")
    print(f"{Colors.GREEN}Total References :{Colors.RESET} {total_references}")
    print(f"{Colors.GREEN}Page Hits :{Colors.RESET} {hit_count}")
    print(f"{Colors.RED}Page Faults :{Colors.RESET} {page_faults}")
    print(f"{Colors.BLUE}Hit Ratio :{Colors.RESET} {hit_ratio:.2%}")
    print(f"{Colors.BLUE}Fault Ratio :{Colors.RESET} {fault_ratio:.2%}")
    print(f"{Colors.PURPLE}Frames Used :{Colors.RESET} {frames}")
    print(f"{Colors.YELLOW}Reference String Length :{Colors.RESET} {len(reference_string)}")


# End of code 