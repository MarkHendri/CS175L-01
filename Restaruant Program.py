#Mark Hendri
#Professoe Eckert
#CS-175L-01
#February 6th, 2023
#Restaraunt Selector Program


def restaurant():
    print("Welcome to the restaurant selector!")
    print("Please answer the following questions.")
    
    vegetarian = input("Is anyone in your party vegetarian? (yes/no): ")
    vegan = input("Is anyone in your party vegan? (yes/no): ")
    gluten_free = input("Is anyone in your party gluten-free? (yes/no): ")

    print("\nBased on your answers, the following restaurants are options:")
    
    if vegetarian == "yes" or vegan == "yes" or gluten_free == "yes":
        if vegetarian == "yes":
            print("- Corner Café")
            print("- Mama's Fine Italian")
            print("- The Chef's Kitchen")
        if vegan == "yes":
            print("- Corner Café")
            print("- The Chef's Kitchen")
        if gluten_free == "yes":
            print("- Main Street Pizza Company")
            print("- Corner Café")
            print("- The Chef's Kitchen")
    else:
        print("- Joe's Gourmet Burgers")
        print("- Main Street Pizza Company")
        print("- Mama's Fine Italian")
        print("- The Chef's Kitchen")

restaurant()
