stack = []

def read_required_string(prompt):
    value = ""
    while not value:
        value = input(prompt).strip()
        if not value:
            print('Error: Value is required')
    return value

def add_plate(stack):
    print('add a plate')
    plate_size = input("Enter a plate size: ").strip()
    if plate_size.isdigit():        #makes sure input value is an int
        plate_size = int(plate_size)
        if plate_size <= 0:     # Error if choose a negative value
            print("Error: Plate size must be a positive integer.")
        elif stack and plate_size > stack[-1]:      # Check to see if plate added is larger than one before
            print(f"Cannot place a plate of size {plate_size} on top of a plate of size {stack[-1]}.")
        else:
            stack.append(plate_size)
            print("Success!")
    else:
        print('Error: Please enter a valid integer')

def print_plates(stack):
    if not stack:
        print("There are no stacked plates.")
    else:
        for plate in reversed(stack):       #flip the stack so largest on bottom
            print('#' * plate)

def remove_plates(stack):
    print('Remove a plate')
    plate_remove = input("How many plates would you like to remove?: ").strip()
    if plate_remove.isdigit():      #makes sure input value is an int
        plate_remove = int(plate_remove)
        if plate_remove <= 0:
            print("Error: You must remove a positive number of plates.")
        elif plate_remove > len(stack):
            print(f"Error: You cannot remove more than {len(stack)} plates. You chose {plate_remove}.")
        else:
            for _ in range(plate_remove):
                stack.pop()
            print("Success!")
    else:
        print('Error: Please enter a valid Integer')


def run():
    option = ""
    while option != '0':
        print('Menu')
        print("================")
        print('0. Exit')
        print('1. Add a plate')
        print('2. Display the stack')
        print('3. Remove a plate')
        option = read_required_string('Select [0-3]: ')
        if option == '0':
            print('Goodbye')
        elif option == '1':
            add_plate(stack)
        elif option == '2':
            print_plates(stack)
        elif option == '3':
            remove_plates(stack)
        else:
            print('I dont understand that command')

if __name__ == '__main__':
    run()