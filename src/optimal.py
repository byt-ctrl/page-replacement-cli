# optimal (OPT/OPR) page replacement algorithm

from typing import List,Set,Tuple
from utils import Colors,print_algorithm_header

class Optimal :
    def __init__(self, frames : int) :
        self.frames=frames
        self.page_list=[]
        self.page_set : Set[int] = set()
        self.page_faults=0
    
    def print_step(self , reference : int , current_index : int , total_references : int , is_fault : bool , victim_page : int = None) -> None :
        step_info=f"Step {current_index + 1}/{total_references}"
        page_info=f"Page: {reference}"
        status = f"{Colors.RED}FAULT{Colors.RESET}" if is_fault else f"{Colors.GREEN}HIT{Colors.RESET}"
        
        frames_display = []
        for a in range(self.frames):
            if a < len(self.page_list):
                frames_display.append(f"[{self.page_list[a]}]")
            else:
                frames_display.append(f"[ ]")
        
        frames_str = " ".join(frames_display)
        victim_info = f" (Replaced : {victim_page})" if victim_page is not None else ""
        
        print(f"{Colors.CYAN}{step_info:<12}{Colors.RESET} | "
              f"{Colors.YELLOW}{page_info:<8}{Colors.RESET} | "
              f"Frames : {frames_str} | "
              f"Status : {status}{victim_info}")

    def find_farthest_page(self , reference_string : List[int] , current_index : int) -> int :
        # find's page that will be used farthest in future
        for page in self.page_list :
            if page not in reference_string[current_index + 1:]:
                return page
        
        farthest_index=-1
        farthest_page=self.page_list[0]
        
        for page in self.page_list :
            try :
                next_index=reference_string.index(page , current_index + 1)
                if next_index > farthest_index :
                    farthest_index = next_index
                    farthest_page = page
            except ValueError :
                return page
        
        return farthest_page
    
    def load_page(self , page : int , reference_string : List[int] , current_index : int) -> Tuple[bool, int] :
        if page in self.page_set :
            return False , None
        
        victim_page=None
        
        if len(self.page_list) >= self.frames :
            victim_page=self.find_farthest_page(reference_string , current_index)
            self.page_list.remove(victim_page)
            self.page_set.remove(victim_page)
        
        self.page_list.append(page)
        self.page_set.add(page)
        self.page_faults += 1
        
        return True , victim_page
    
    def run(self,reference_string : List[int]) -> int :
        print_algorithm_header("Optimal Page Replacement Algorithm")
        
        self.page_list=[]
        self.page_set=set()
        self.page_faults=0
        
        total_references=len(reference_string)
        
        for a , page in enumerate(reference_string) : 
            is_fault, victim_page = self.load_page(page, reference_string, a)
            self.print_step(page, a, total_references, is_fault, victim_page)
        
        return self.page_faults
    
# End of code