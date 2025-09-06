# FIFO (First-In-First-Out) Page Replacement Algorithm

from utils import Colors,print_algorithm_header
from typing import List,Set

class FIFO :
    def __init__(self,frames : int):
        self.frames=frames
        self.page_queue = []
        self.page_set : Set[int] = set()
        self.page_faults=0
    
    def print_step(self, reference: int, current_index: int, total_references: int, is_fault: bool) -> None:
        step_info = f"Step {current_index + 1}/{total_references}"
        page_info = f"Page : {reference}"
        status = f"{Colors.RED}FAULT{Colors.RESET}" if is_fault else f"{Colors.GREEN}HIT{Colors.RESET}"
        
        frames_display = []
        for a in range(self.frames):
            if a < len(self.page_queue):
                frames_display.append(f"[{self.page_queue[a]}]")
            else:
                frames_display.append(f"[ ]")
        
        frames_str = " ".join(frames_display)
        
        print(f"{Colors.CYAN}{step_info:<12}{Colors.RESET} | "
              f"{Colors.YELLOW}{page_info:<8}{Colors.RESET} | "
              f"Frames : {frames_str} | "
              f"Status : {status}")
    
    def load_page(self, page: int) -> bool:
        is_fault = page not in self.page_set
        
        if not is_fault:
            return False
        
        if len(self.page_queue) >= self.frames:
            removed_page = self.page_queue.pop(0)
            self.page_set.remove(removed_page)
        
        self.page_queue.append(page)
        self.page_set.add(page)
        self.page_faults += 1
        
        return True
    
    def run(self, reference_string: List[int]) -> int:
        print_algorithm_header("FIFO Page Replacement Algorithm")
        
        self.page_queue = []
        self.page_set = set()
        self.page_faults = 0
        
        total_references = len(reference_string)
        
        for a, page in enumerate(reference_string) :
            is_fault=self.load_page(page)
            self.print_step(page, a, total_references, is_fault)
        
        return self.page_faults