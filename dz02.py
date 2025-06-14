import random

def get_numbers_ticket(min, max, quantity):
    
    if (not isinstance(min, int)
        or not isinstance(max, int)
        or not isinstance(quantity, int)
        or min < 1
        or max > 1000
        or min > max
        or quantity <= 0
        or quantity > (max - min + 1)):
        return []

    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)



