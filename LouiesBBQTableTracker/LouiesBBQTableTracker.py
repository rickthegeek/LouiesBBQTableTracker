#Project: CIS 177 WEEK 9 PROJECT
#Project Location: projects\cis177\LouiesBBQTracker
#File: LouiesBBQTracker.py
#Purpose: Keep track of a reservation list at Louie's BBQ,
#         keeping a VIP list as well
#Revision: 1.0 / 27 MAR 2017
#Created: 27 MAR 2017
#Author: Rick Miller <rick@rickthegeek.com>

waitlist = [] # This will be the waiting list for Louie's BBQ

# This function will add a name to the end of the list. list.append will add the entry to the end of the list
# NOTE: For accuracy, all user entries are converted to and stored as upper case, this will allow unambiguous entry of
# a name to remove or find in other functions. This is becuse "smith", "Smith", "SMITH" and "SmItH" are all different
# strings in python.
def add_name(my_list):
    nameToAdd = input('Enter the party\'s name to add: ').upper()
    my_list.append(nameToAdd)

# This function will add a name to the beginning of the given list. Note that list.insert(0) will add the entry
# as the first entry in the list. Note that each VIP is simply added to the beginning of the list, without keeping
# a separate VIP list
def add_VIP(my_list):
    nameToAdd = input('Enter the VIP party\'s name to add: ').upper()
    my_list.insert(0, nameToAdd)

# This name will remove a name from the given list. Note that the index function will return the first instance of the
# entered name. It's up to the user to keep track of which real-life "smith" the user is sending away, for instance.
def remove_name(my_list):
    nameToRemove = input('Enter the name to remove: ').upper()
    if nameToRemove in my_list: # is the name on the list at least once?
        indexToRemove = my_list.index(nameToRemove) # if it is, then remove the first instance of that name
        my_list.pop(indexToRemove)
    else: # the name isn't on the list so tell the user
        print('Sorry,', nameToRemove,'not on the list.')

def table_ready(my_list):
    if len(my_list) > 0: # make sure the list isn't empty!
        tableName = my_list[0] # get the next name on the list
        print('A table is now ready for',tableName,'and that name has been removed from the list') # tell the user...
        my_list.pop(0) # ...and remove the name from the list
    else: # the list is empty, so tell the user
        print('\nEMPTY')

def print_list(my_list):
    if len(my_list) > 0: # is there at least one name on the list?
        print('\nCurrent list:') # if there is, print a header
        print('-------------')
        for name in my_list: # then for each name on the list...
            print(name) # ...print the names, one per line
    else: # nothing on the list, so tell the user
        print('\nEMPTY')

def print_next_name(my_list):
    if len(my_list) > 0: # if the list isn't empty
        print('The next name on the list is:', my_list[0]) # ...so tell the user who the next person on the list is
    else: # the list is empty
        print('\nEMPTY') # ...so tell the user

# *** MAIN LOOP STARTS HERE! ***

userChoice = ''

while userChoice != 'q': # this loop will repeat until the user selects 'q'
    print('\nLouie\'s BBQ Restaurant Reservation System') # print the menu
    print('\nMain Menu\n')
    print('A - Add a name to the list')
    print('V - Add a VIP to the list')
    print('R - Remove a name from the list')
    print('P - Print the list')
    print('N - Print the next party to get a table')
    print('T - Assign a table to the next party on the list')
    print('Q - Quit the program')
    userChoice = input('Please enter yout selection: ')[0].lower()
    if userChoice in ('a', 'v', 'r', 'p', 'n', 't', 'q'): # check if the user has entered a valid choice
        if userChoice == 'a': # if the user has enetered a valid choice, go to the right function
            add_name(waitlist)
        elif userChoice == 'v':
            add_VIP(waitlist)
        elif userChoice == 'r':
            remove_name(waitlist)
        elif userChoice == 't':
            table_ready(waitlist)
        elif userChoice == 'p':
            print_list(waitlist)
        elif userChoice == 'n':
            print_next_name(waitlist)
    else: # the user didn't make a valid choice. Note that 'q' is a valid choice but will bypass this message
        print('Sorry, invalid choice. Try again!')
print('End of program') # user chose 'q' so the program ends here.
