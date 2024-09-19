# Global variable initialized
global_variable = 100

# Dictionary with initial key and values
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Function to process numbers and appending them to a list
# Fixed the function name from 'prosse_numbers' to 'process_numbers'
def process_numbers():
    global global_variable  # Ensure we modified the global variable
    # Fixed variable name  from 'global_global_variable' to 'global_variable'
    global_variable = 5  # This variable was redundant but kept as part of a structure
    numbers = [1, 2, 3, 4, 5]  # List of initial numbers
    # Changed 'repose' to 'append' since lists use append to add a items
    while global_variable > 0:
        if global_variable >= 0:
            numbers.append(global_variable)  # Corrected to appending the global variable to the list
            global_variable -= 1  # Decrement of the global variable
    return numbers

# List with a repeated numbers
my_set = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

# Calling corrected process_numbers function without the arguments
result = process_numbers()

# Function to modify the dictionary by adding new key-value pair
# Fix the function name from 'moldfy_dict' to 'modify_dict'
def modify_dict():
    global global_variable  # Using global variable within the function
    global_variable = 10  # Updating global variable
    my_dict['key4'] = global_variable  # Add new key-value pair to the dictionary

# Call modify_dict to updating the dictionary
modify_dict()

# Function to checking and update global values
# Fixed the function name from 'upacte_global' to 'update_global'
def update_global():
    global global_variable  # Use global variable
    global_variable = 10  # Reset global variable to 10
    # Changed the key check from integer 5 to the correct key 'key4'
    if 'key4' not in my_dict:
        print("Key not found in the dictionary!")  # Corrected the message
    print(global_variable)  # Print the global variable
    print(my_dict)  # Print the updated dictionary
    print(my_set)  # Print the list

# Call update_global to printing results
update_global()
