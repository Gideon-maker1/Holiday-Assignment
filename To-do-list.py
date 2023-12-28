#infinite loop
print('***Welcome to my to-do-list.***')
print()
todos = []

#function to add an activity to a list
def ADD():
    activity = input('Enter the activity you want to add:\n')
    todos.append(activity)
    print(f'{activity} has been added successfully.')

#function to update an item in a list
def UPDATE():
    index = int(input('Enter the index of the item you want to update:\n'))
    if index < len(todos):
        new_activity = input('Enter new activity:\n')
        todos[index] = new_activity
        print('Activity updated successfully')
    else:
        print('Invalid index or list empty.')

#function to delete an item in a list
def DEL():
        index = int(input('Enter the index of the activity you want to delete:\n'))
        if index < len(todos):
            del todos[index]
            print('Activity deleted successfully')
        else:
            print('Invalid index or list already empty.')

#function to view an item in a list
def VIEW():
     if not todos:
          print('Nothing to view, kindly add something.')
     else:
          print(todos)

#function to exit the program
def EXIT():
     print('Thank you for using my to-do-list.\n'
           'Exiting program...\n'
           'GOODBYE...')
     exit(1)

#main program
while True:
    user_choice = int(input('select 1 to ADD.\n'
                            'select 2 to UPDATE.\n'
                            'select 3 to DELETE.\n'
                            'select 4 to VIEW.\n'
                            'select 5 to EXIT.\n'))
    if user_choice == 1:
         ADD()
    elif user_choice == 2:
         UPDATE()
    elif user_choice == 3:
         DEL()
    elif user_choice == 4:
         VIEW()
    elif user_choice == 5:
         EXIT()
    else:
         print('Invalid choice.')