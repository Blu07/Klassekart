
def get_postive_int(prompt: str) -> int:
    """
    Prompt the user for a positive integer until valid input is received.
        
    :param prompt: The prompt message to display to the user
    :type prompt: str
    
    :return: A positive integer entered by the user
    :rtype: int
    """
    
    valid = False
    value = 0
    
    while not valid:
        try:
            value: int = int(input(prompt))
            
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            
            valid = True
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    return value