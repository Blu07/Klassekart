

def get_postive_int(prompt: str) -> int:
    """
    Prompt the user for a positive integer until valid input is received.
        
    :param prompt: The prompt message to display to the user
    :type prompt: str
    
    :return: A positive integer entered by the user
    :rtype: int
    """
    
    while True:
        try:
            value: int = int(input(prompt))
            
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            
            return value
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
