from typing import List

def load_numbers_sorted(txt: str) -> List[int]:
    numbers = []
    
    with open(txt) as f:
        numbers = sorted(map(lambda e: int(e), f))
    
    return numbers
