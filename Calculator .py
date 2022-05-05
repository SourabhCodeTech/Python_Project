import keyboard

number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))
print("Your Press A Button on your keyboard So Number1 and Number2 is Added")
print("Your Press S Button on your keyboard So Number1 and Number2 is Subtracted")
print("Your Press M Button on your keyboard So Number1 and Number2 is Multiply")
print("Your Press D Button on your keyboard So Number1 and Number2 is Division")

while True:
    try:
        if keyboard.is_pressed("A"):
            print("\nYou are Press A and Answer: ", number1 + number2)
            break
        if keyboard.is_pressed("S"):
            print("\nYou are Press S and Answer: ", number1 - number2)
            break
        if keyboard.is_pressed("M"):
            print("\nYou are Press M and Answer: ", number1 * number2)
            break
        if keyboard.is_pressed("D"):
            print("\nYou are Press D and Answer: ", number1 / number2)
            break
    except:
        break