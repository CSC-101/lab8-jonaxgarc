# Task 1

def groups_of_3 (original:list[int]) -> list[list[int]]:
    trio = [] # Placeholder list that will be returns later on
    for i in range(0, len(original), 3): # For loop that goes through every third value in the list original
        trio.append(original[i:i+3]) # Would append to the trio list the element from i to i+2
    return trio # Returns the trio list

# Task 2

def water_bill(gallons:int):
    price=0
    if gallons>1000:
