# Restaurent Menu..
print("----- MENU -----")
print("1. Biryani")
print("2. Chicken 65")
print("3. Veg Pulao")
print("4. Butter Chicken")
print("5. Paneer Tikka")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Item : Biryani")
        print("Price : ₹250")
    case 2:
        print("Item : Chicken 65")
        print("Price : ₹180")
        print("Description : Crispy and spicy deep-fried chicken pieces.")
    case 3:
        print("Item : Veg Pulao")
        print("Price : ₹150")

    case 4:
        print("Item : Butter Chicken")
        print("Price : ₹280")
    case 5:
        print("Item : Paneer Tikka")
        print("Price : ₹200")
    case _:
        print("Invalid choice")