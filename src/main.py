import sys
import time
from lru import LRU
from fifo import FIFO
from optimal import Optimal
from typing import List
from utils import Colors,clear_screen,print_header,print_success,print_error,print_warning,print_info

def get_reference_string() -> List[int] :
    while True :
        try:
            print_info("Enter the reference string (space-separated integers)")
            print_info("Example: 1 2 3 4 1 2 5 1 2 3 4 5")
            user_input=input(f"{Colors.CYAN}>>> {Colors.RESET}").strip()
            
            if not user_input :
                print_error("Reference string cannot be empty . Please try again .")
                continue
            
            reference_string=list(map(int,user_input.split()))
            
            if len(reference_string) < 1 :
                print_error("Reference string must contain at least one page . Please try again.")
                continue
            
            return reference_string
        except ValueError :
            print_error("Please enter only integers separated by spaces. Try again.")
        except KeyboardInterrupt :
            print(f"\n{Colors.YELLOW}Program interrupted by user.{Colors.RESET}")
            sys.exit(0)

def get_number_of_frames() -> int :
    while True :
        try:
            print_info("Enter the number of frames (1-20 recommended)")
            frames = int(input(f"{Colors.CYAN}>>> {Colors.RESET}"))
            if frames <= 0:
                print_error("Number of frames must be a positive integer. Please try again.")
                continue
            elif frames > 50:
                print_warning("Large number of frames detected. This may affect display readability.")
                confirm = input(f"{Colors.YELLOW}Continue anyway? (y/n): {Colors.RESET}").strip().lower()
                if confirm not in ['y', 'yes']:
                    continue
            return frames
        except ValueError:
            print_error("Please enter a valid integer for the number of frames. Try again.")
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Program interrupted by user.{Colors.RESET}")
            sys.exit(0)

def get_algorithm_choice() -> str:
    print_header("Choose the algorithm to run:")
    print(f"{Colors.GREEN}1.{Colors.RESET} FIFO (First-In-First-Out)")
    print(f"{Colors.GREEN}2.{Colors.RESET} LRU (Least Recently Used)")
    print(f"{Colors.GREEN}3.{Colors.RESET} OPR/OPT (Optimal)")
    print(f"{Colors.GREEN}4.{Colors.RESET} Compare All Algorithms")
    print(f"{Colors.GREEN}5.{Colors.RESET} Help")
    
    while True:
        try : 
            choice = input(f"{Colors.CYAN}Enter your choice (1-5): {Colors.RESET}").strip()
            if choice in ['1', '2', '3', '4', '5']:
                return choice
            else:
                print_error("Please enter 1, 2, 3, 4, or 5 for your choice. Try again.")
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Program interrupted by user.{Colors.RESET}")
            sys.exit(0)

def show_help() :
    clear_screen()
    print_header("Algorithm Help")
    
    print(f"{Colors.CYAN}FIFO (First-In-First-Out):{Colors.RESET}")
    print("  - Replaces the oldest page in memory")
    print("  - Simple to implement but can suffer from Belady's anomaly")
    print()
    
    print(f"{Colors.CYAN}LRU (Least Recently Used):{Colors.RESET}")
    print("  - Replaces the page that hasn't been used for the longest time")
    print("  - More efficient than FIFO but harder to implement")
    print()
    
    print(f"{Colors.CYAN}OPT (Optimal):{Colors.RESET}")
    print("  - Replaces the page that won't be used for the longest time in future")
    print("  - Theoretical optimal algorithm (impossible to implement in practice)")
    print("  - Used as a benchmark for other algorithms")
    print()
    
    input(f"{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")

def run_single_algorithm(choice: str, reference_string: List[int], frames: int) -> None:
    algorithms={
        '1': FIFO,
        '2': LRU,
        '3': Optimal
    }
    
    algorithm_names = {
        '1': 'FIFO (First-In-First-Out)',
        '2': 'LRU (Least Recently Used)',
        '3': 'Optimal'
    }
    
    if choice in algorithms :
        algorithm=algorithms[choice](frames)
        algorithm_name=algorithm_names[choice]
        
        print_header(f"Running {algorithm_name} Algorithm")
        time.sleep(0.5)
        
        page_faults = algorithm.run(reference_string)
        
        print_header("Results Summary")
        print(f"{Colors.GREEN}Algorithm:{Colors.RESET} {algorithm_name}")
        print(f"{Colors.GREEN}Reference String:{Colors.RESET} {' '.join(map(str, reference_string))}")
        print(f"{Colors.GREEN}Number of Frames:{Colors.RESET} {frames}")
        print(f"{Colors.RED}Total Page Faults:{Colors.RESET} {page_faults}")
        print(f"{Colors.BLUE}Total References:{Colors.RESET} {len(reference_string)}")
        print(f"{Colors.PURPLE}Page Fault Ratio:{Colors.RESET} {page_faults/len(reference_string):.2%}")

def run_comparison(reference_string : List[int] , frames : int) -> None :
    print_header("Algorithm Comparison")
    print(f"{Colors.BLUE}Reference String :{Colors.RESET} {' '.join(map(str,reference_string))}")
    print(f"{Colors.BLUE}Number of Frames :{Colors.RESET} {frames}")
    print()
    
    algorithms = [
        (FIFO(frames),"FIFO"),
        (LRU(frames),"LRU"),
        (Optimal(frames),"OPTIMAL")
    ]
    
    results=[]
    
    for algorithm , name in algorithms :
        print_header(f"Running {name} Algorithm")
        time.sleep(0.3)
        page_faults=algorithm.run(reference_string)
        results.append((name,page_faults))
        print()
    
    print_header("Comparison Results")
    print(f"{'Algorithm':<15} {'Page Faults':<15} {'Efficiency':<15}")
    print("-" * 45)
    
    min_faults = min(results,key=lambda x: x[1])[1]
    
    for name , faults in results :
        efficiency = "Best" if faults==min_faults else f"{((min_faults/faults)*100):.1f}%"
        color = Colors.GREEN if faults==min_faults else Colors.RESET
        print(f"{color}{name:<15}{Colors.RESET} {faults:<15} {efficiency:<15}")

def run_algorithm(choice : str , reference_string : List[int], frames: int) -> None :
    if choice=='4' :
        run_comparison(reference_string , frames)
    elif choice=='5' :
        show_help()
        return
    else :
        run_single_algorithm(choice , reference_string , frames)

def get_continue_choice() -> str :
    while True :
        try :
            print()
            print(f"{Colors.CYAN}What would you like to do?{Colors.RESET}")
            print(f"{Colors.GREEN}1.{Colors.RESET} Run another simulation")
            print(f"{Colors.GREEN}2.{Colors.RESET} Change current settings")
            print(f"{Colors.GREEN}3.{Colors.RESET} Exit")
            
            choice = input(f"{Colors.CYAN}Enter your choice (1-3): {Colors.RESET}").strip()
            if choice in ['1', '2', '3']:
                return choice
            else:
                print_error("Please enter 1, 2, or 3. Try again.")
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Program interrupted by user.{Colors.RESET}")
            sys.exit(0)

def main() :
    clear_screen()
    print_header("Page Replacement Algorithm Solver")
    print(f"{Colors.YELLOW}Enhanced Version with Colors and Advanced Features{Colors.RESET}")
    print("=" * 60)
    
    reference_string=None
    frames=None
    
    try :
        while True :
            if reference_string is None :
                reference_string=get_reference_string()
            
            if frames is None :
                frames=get_number_of_frames()
            
            choice=get_algorithm_choice()
            
            if choice=='5' :
                show_help()
                continue
            
            run_algorithm(choice,reference_string,frames)
            
            continue_choice = get_continue_choice()
            
            if continue_choice == '1' :
                clear_screen()
                print_header("Page Replacement Algorithm Solver")
                continue
            elif continue_choice == '2' :
                reference_string=None
                frames=None
                clear_screen()
                print_header("Page Replacement Algorithm Solver")
                continue
            else :
                print_success("Thank you for using the Page Replacement Algorithm Solver!")
                break
                
    except KeyboardInterrupt :
        print(f"\n{Colors.YELLOW}Program interrupted by user.{Colors.RESET}")
        sys.exit(0)
    except Exception as e :
        print_error(f"An unexpected error occurred: {e}")
        sys.exit(1)

main()