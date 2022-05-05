# Health Management System
lo_re = input("Log Karna Chataho | Receive Karna Chataho: ").capitalize()
name = input("Enter Username: ").capitalize()
food_exer = input("Food Log Karna Chataho | Exercise Log Karna Chataho: ").capitalize()
if lo_re == "Log":
    if name == name:
        if food_exer == "Food":
            food = input("Enter Food Name: ")
            create_file = open(f"health/{name}_Food_Name.txt", "a")
            create_file.write(food)
            print("Successfully Right")
        elif food_exer == "Exercise":
            Exercise = input("Enter Exercise Name: ")
            create_file = open(f"health/{name}_Exercise_Name.txt", "a")
            create_file.write(Exercise)
            print("Successfully Right")
elif lo_re == "Receive":
    if name == name:
        if food_exer == "Food":
            read_file = open(f"health/{name}_Food_Name.txt", "r")
            print(read_file.read())
        elif food_exer == "Exercise":
            read_file = open(f"health/{name}_Exercise_Name.txt", "r")
            print(read_file.read())

