import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    
    # Initializing pool for numbers 
    lottery_numbers = []
    
    # Checking numbers validity, assuming those are integers
    # (still vulnerable to other types)
    # AND sample won't exceed range
    if (1 <= min < max <= 1000 and 0 < quantity <= (max - min)):

        # Sampling unique numbers from defined range
        lottery_numbers = random.sample(range(min, max + 1), quantity)
        return sorted(lottery_numbers)
    else:
        return lottery_numbers