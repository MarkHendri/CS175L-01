#Mark Hendri
#Professor Eckert
#CS 175 01
#2/13/23

def restaurant():
    vegetarian = False
    vegan = False
    gluten_free = False

    while True:
        response = input("Are any members of your party vegetarian? (yes/no) ")
        if response == "yes":
            vegetarian = True
            break
        elif response == "no":
            break
        else:
            print("Invalid response. Please try again.")

    while True:
        response = input("Are any members of your party vegan? (yes/no) ")
        if response == "yes":
            vegan = True
            break
        elif response == "no":
            break
        else:
            print("Invalid response. Please try again.")

    while True:
        response = input("Are any members of your party gluten-free? (yes/no) ")
        if response == "yes":
            gluten_free = True
            break
        elif response == "no":
            break
        else:
            print("Invalid response. Please try again.")

    print("\nHere are the restaurants that meet your dietary restrictions:")

    if vegetarian and not vegan and not gluten_free:
        print("- Main Street Pizza Company")
        print("- Mama's Fine Italian")
    elif vegetarian and vegan and not gluten_free:
        print("- Corner Café")
        print("- The Chef's Kitchen")
    elif vegetarian and not vegan and gluten_free:
        print("- Main Street Pizza Company")
        print("- Corner Café")
        print("- The Chef's Kitchen")
    elif vegetarian and vegan and gluten_free:
        print("- Corner Café")
        print("- The Chef's Kitchen")
    elif not vegetarian and not vegan and gluten_free:
        print("- Main Street Pizza Company")
        print("- Corner Café")
        print("- The Chef's Kitchen")
    else:
        print("- Joe's Gourmet Burgers")
        print("- Main Street Pizza Company")
        print("- Mama's Fine Italian")

restaurant()
