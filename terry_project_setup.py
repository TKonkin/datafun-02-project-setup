"""
Module: terry_project_setup

Purpose: Provide functions to script project folders (and domonstrate basic Python coding skills).

Description: This module provides functions for creating a series of project folders.

Author: Terry Konkin

TODO: Change the module name in this opening docstring
TODO: Change the author in this opening docstring
"""

#####################################
# Import Modules at the Top
#####################################

# Import moduldes from standand library
# TODO: Import additional modules as needed
import pathlib


# Import local modules
# TODO: Change this to import your module and uncomment
import utils_terry 

#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    # TODO: Implement the actual folder creation logic
    
    for year in range(start_year, end_year + 1):
        folder_name = data_path.joinpath(str(year))
        folder_name.mkdir(exist_ok=True)
        print(f"Folder {folder_name} created.")
    pass

  
#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    # TODO: Add docstring
    """
    Create folders from a given list of names.

    Arguments:
    folder_list -- the list of folder names.
    to_lowercase -- revises the file name to all lower case.
    remove_spaces -- removes spaces from between words in the file name.
    """
    # TODO: Log the function call and its arguments

    print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}")
    
    # TODO: Implement this function and remove the temporary pass

    if to_lowercase:
        folder_list = [name.lower() for name in folder_list]    

    if remove_spaces:   
        folder_list = [name.replace(" ", "") for name in folder_list]

    for f_name in folder_list:
        folder_name=data_path.joinpath(f_name)
        folder_name.mkdir(exist_ok=True)
        print(f"Folder {folder_name} created.")
  
#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    # TODO: Implement this function professionally and remove the temporary pass
    """
    Create folders from a given list of names, with all folder names containing a common prefix.
    
    Arguments:
    folder_list -- the list of folder names.
    prefix -- the prefix to appear before each folder name.

    """
    # Log the function call and its arguments

    print(f"FUNCTION CALLED: create_prefixed_folders with folder_list={folder_list} and prefix={prefix}")

    # Implement this function
    
    for fold_name in folder_list:
        prefix_name = f"{prefix} - {fold_name}"
        folder_name=data_path.joinpath(prefix_name)
        folder_name.mkdir(exist_ok=True)
        print(f"Folder {folder_name} created.")
    
    pass

  

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(folder_list: list, duration_seconds: int) -> None:
    # TODO: Implement this function professionally and remove the temporary pass

    """
    Create folders periodically.

    Arguments:
    folder_list -- the list of folder names.
    duration_seconds -- the duration in seconds between folder creation.

    """
    # Log the function call and its arguments

    print(f"FUNCTION CALLED: create_folders_periodically with duration_seconds={duration_seconds}")

    # Implement this function

    import os
    import time

    for f_name in folder_list:
        folder_name=data_path.joinpath(f_name)
        folder_name.mkdir(exist_ok=True)
        print(f"Folder {folder_name} created.")

        print(f"Now wait {duration_seconds} before creating the next folder")
        time.sleep(duration_seconds)  

    pass


  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    # TODO: Change this to use your module function and uncomment
    # print(f"Byline: {utils_terry.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    folder_names = ["fn4_test1", "fn4_test2", "fn4_test3"]
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(folder_names, duration_secs)

    # TODO: Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    # Uncomment this line after you've added your custom logic
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

#TODO: Run this as a script to test that all functions work as intended.