# Lauren Corradino, Kyle Mrosko, Scottie Taylor, Braedon Lindsey
# ENGR 102-212
# Assignment: Lab3_Act2.py


# Inputting names and birthdays with proper formatting
name1 = input("User 1, enter your name: ").ljust(20)
birthday1 = input("User 1, enter your birthday: ")
name2 = input("User 2, enter your name: ").ljust(20)
birthday2 = input("User 2, enter your birthday: ")
name3 = input("User 3, enter your name: ").ljust(20)
birthday3 = input("User 3, enter your birthday: ")
name4 = input("User 4, enter your name: ").ljust(20)
birthday4 = input("User 4, enter your birthday: ")

# Printing names and birthdays with proper formatting
print("\n\n" + "Names:".ljust(20) + "Birthdays: " + "\n")
print(name1.capitalize() + birthday1)
print(name2.capitalize() + birthday2)
print(name3.capitalize() + birthday3)
print(name4.capitalize() + birthday4)