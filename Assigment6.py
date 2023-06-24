def ds(roll_no, name):
    # Create a list and add values
    my_list = []
    my_list.append(roll_no)
    my_list.append(name)
    print("List:", my_list)

    # Create a tuple and add values
    my_tuple = (roll_no, name)
    print("Tuple:", my_tuple)

    # Create a set and add values
    my_set = set()
    my_set.add(roll_no)
    my_set.add(name)
    print("Set:", my_set)

    # Create a dictionary and add values
    my_dict = {}
    my_dict['Roll No'] = roll_no
    my_dict['Name'] = name
    print("Dictionary:", my_dict)

    # Change values during runtime
    new_roll_no = input("Enter new roll number: ")
    new_name = input("Enter new name: ")

    my_list[0] = new_roll_no
    my_list[1] = new_name
    print("Updated List:", my_list)

    # Note: Tuples are immutable, so we need to convert it to a list and then back to a tuple with updated values
    my_tuple = list(my_tuple)
    my_tuple[0] = new_roll_no
    my_tuple[1] = new_name
    my_tuple = tuple(my_tuple)
    print("Updated Tuple:", my_tuple)

    my_set.remove(roll_no)
    my_set.add(new_roll_no)
    my_set.remove(name)
    my_set.add(new_name)
    print("Updated Set:", my_set)

    my_dict['Roll No'] = new_roll_no
    my_dict['Name'] = new_name
    print("Updated Dictionary:", my_dict)

    # Delete the data structures
    del my_list
    del my_tuple
    del my_set
    del my_dict
    print("Data structures deleted.")


# Test the function
roll = input("Enter roll number: ")
student_name = input("Enter student name: ")
ds(roll, student_name)
