# Assignment #2
# INF1340 Section 2
# Fall-2017
# Mateus Macedo


# MENU FUNCTION
def menu(inventory_size):
    ''' (int) -> str
    Return the menu selection from the user based on the inventory size. 
    
    >>> menu(0)
    Car Inventory Menu
    ==================

    1- Add a Car
    Q- Quit

    Enter your selection:
    
    >>> menu(1)
    Car Inventory Menu
    ==================

    1- Add a Car
    2- Remove a Car
    3- Find a Car
    4- Show Complete Inventory
    Q- Quit

    Enter your selection: 
    
    >>> menu(5)
    Car Inventory Menu
    ==================

    1- Add a Car
    2- Remove a Car
    3- Find a Car
    4- Show Complete Inventory
    Q- Quit

    Enter your selection: 
    '''
    # Get and return user input when the lenght of the inventory is 0
    if len(inventory) == 0:
        print('\nCar Inventory Menu\n================== \n1- Add a Car \nQ- Quit')
        selection = input('\nEnter your selection: ')
        
        return selection
    
    # Get and return user input when the lenght of the inventory is greater than 0        
    elif len(inventory) > 0:  
        print('\nCar Inventory Menu\n================== \n\n1- Add a Car \n2- Remove a Car\n3- Find a Car\n4- Show Complete Inventory\nQ- Quit')
        selection = input('\nEnter your selection: ')
        
        return selection
    

#FIND INDEX FUNCTION  
def find_index(inventory, model_number, year, colour):
    ''' (list, str, int, str) -> int  
    
    Return the car index correspondent to the matching model number, year and colour. If there is no match, return -1.
    
    >>>inventory = [['ZN3EU', 2017, 'Red', 'Toyota', 'Prius V', 'Hatchback', 1]]
    >>>find_index(inventory, 'EK13Z', 2013, 'Black')
    -1
   
    >>>inventory = [['ZN3EU', 2017, 'Red', 'Toyota', 'Prius V', 'Hatchback', 1]]
    >>>find_index(inventory, 'ZN3EU', 2017, 'Red')
    0
    '''
    # start result at -1 
    result = -1    
    
    # if car index is a match in inventory, assign index to result 
    for i in inventory: 
        if model_number == i[0] and year == i[1] and colour == i[2]:
            result = inventory.index(i)
            
    return result
        
 
# ADD CAR FUNCTION       
def add_car(inventory):
    '''(list) -> None
    Add car to inventory iff a car with the same model number, year, and colour is not already part of the inventory. If a car with the same model number, year, and colour is already part of the inventory, the function asks the user the quantity to be added and increases the quantity accordingly. 
    
    >>>add_car(inventory)
    None
    '''
    model_number = input('\nEnter the model number: ')
    year = int(input('Enter the year: '))
    colour = input('Enter the colour: ')  
    
    index = find_index(inventory, model_number, year, colour)
    
    # modify inventory quantity by the amount input by user if car is on inventory and print new quantity  
    if index != -1:
        print('\nCar already exist in inventory.\n')
        quantity = int(input('Enter the quantity to be added: '))
        
        # modify inventory quantity by the amount input from user
        inventory[index][6] = inventory[index][6] + quantity
        
        print('Increased quantity by ' + str(quantity) + '.  New quantity is:', inventory[index][6],'\n')  
    
    # add new car to inventory using the user input if car is not on inventory and print success
    else:
        make = input('Enter the make: ')
        model = input('Enter the model: ')
        body_type = input('Enter the body type: ')
        quantity = int(input('Enter the quantity: '))
        
        inventory.append([model_number, year, colour, make, model, body_type, quantity])
        
        print('\nNew car successfully added.')
            

# REMOVE CAR FUNCTION       
def remove_car(inventory):
    '''(list) -> None
    Remove car from inventory if and only if a car quantity is one. If quantity is greater than one, decrease the quantity of the car by one. 
    
    >>>remove_car(inventory)
    None
    ''' 
    model_number = input('\nEnter the model number: ')
    year = int(input('Enter the year: '))
    colour = input('Enter the colour: ')   
    
    index = find_index(inventory, model_number, year, colour)
    
    if index != -1:
        # remove car from inventory at index "index" if car quantity is 1
        if inventory[index][6] == 1:
            inventory.pop(index)
            
            print('\nCar removed from inventory.\n')
        
        # reduce inventory quantity by 1 at index "index" if car quantity is greater than 1   
        else:
            inventory[index][6] = inventory[index][6] - 1
            
            print("\nDecreased quantity by 1. New quantity is: " + str(inventory[index][6]) + '\n')
            
    # if car is not on inventory
    else: 
        print('\nCar not found! Cannot remove car!\n')
        
            
            
#FIND CAR FUNCTION       
def find_car(inventory):
    '''(list) -> None
    Prompt user if they want to find a car in the inventory by Model Number, Make, Model, or Body Type.  
    
    >>>find_car(inventory)
    None
    '''
    
    print('\nSearch Menu\n===========\n\n1- Search by Model Number\n2- Search by Make\n3- Search by Model\n4- Search by Body Type')
    
    selection = int(input('\nEnter your selection: '))
     
    # keep prompting user input while selection is greater than 4 or less than 1               
    while selection > 4 or selection < 1:
        print('Wrong selection, try again!')
        
        selection = int(input('\nEnter your selection: '))
    
    if selection == 1:
        model_number = input('Enter the model number: ')
        
        # not found starting value
        not_found = True
        
        # if model number is a match in inventory, print i 
        for i in range(len(inventory)):
            if model_number == inventory[i][0]:
                not_found = False
                
                print(inventory[i][0],'\t',inventory[i][1],'\t',inventory[i][2],'\t',inventory[i][3],'\t',inventory[i][4],'\t',inventory[i][5],'\t',inventory[i][6])
                
        # if the model number is not a match in inventory                                  
        if not_found:
                print('\nNo cars found!')
                
    elif selection == 2:
        make = input('Enter the make: ')
        
        # not found starting value
        not_found = True
        
        # if make is a match in inventory, print i
        for i in range(len(inventory)):
            if make == inventory[i][3]:
                not_found = False
                print(inventory[i][0],'\t',inventory[i][1],'\t',inventory[i][2],'\t',inventory[i][3],'\t',inventory[i][4],'\t',inventory[i][5],'\t',inventory[i][6])
        
        # if make is not a match in inventory         
        if not_found:
            print('\nNo cars found!')            

    elif selection == 3:
        model = input('Enter the model: ')
        
        # not found starting value
        not_found = True
        
        # if model is a match in inventory, print i
        for i in range(len(inventory)):
            if model == inventory[i][4]:
                not_found = False
                print(inventory[i][0],'\t',inventory[i][1],'\t',inventory[i][2],'\t',inventory[i][3],'\t',inventory[i][4],'\t',inventory[i][5],'\t',inventory[i][6]) 
        
        # if model is not a match in inventory           
        if not_found: 
            print('\nNo cars found!')            
                
    elif selection == 4:
        body_type = input('Enter the body type: ')
        
        # not found starting value
        not_found = True
        
        # if body type is a match in inventory, print i
        for i in range(len(inventory)):
            if body_type == inventory[i][5]:
                not_found = False
                print(inventory[i][0],'\t',inventory[i][1],'\t',inventory[i][2],'\t',inventory[i][3],'\t',inventory[i][4],'\t',inventory[i][5],'\t',inventory[i][6])
         
        # if body type is not a match in inventory        
        if not_found: 
            print('\nNo cars found!')            
        
                
#SHOW INVENTORY FUNCTION
def show_inventory(inventory):
    '''(list) -> None
    Print all car data one car per line. 
    
    >>> show_inventory(inventory)
    None
    '''
    print('\nComplete Inventory:\n==================\n')
    
    # Display inventory
    for i in range(len(inventory)):
        print(inventory[i][0],'\t',inventory[i][1],'\t',inventory[i][2],'\t',inventory[i][3],'\t',inventory[i][4],'\t',inventory[i][5],'\t',inventory[i][6])
        
    print('\n')
        
                
#MAIN FUNCTION
inventory = []
selection = menu(len(inventory))

# Call different functions based on user input
while selection != 'q' and selection != 'Q':
    if selection == '1':       
        add_car(inventory)
        
    elif len(inventory) == 0 or selection < '0' or selection > '4':
        print('Wrong Selection, try again!') 
        
    elif selection == '2':        
        remove_car(inventory)
        
    elif selection == '3':        
        find_car(inventory)
        
    elif selection == '4':
        show_inventory(inventory)
        
    selection = menu(len(inventory))
    
print('Goodbye!')
        
    



