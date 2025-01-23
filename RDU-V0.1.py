programVersion = "V0.1"
print("Welcome to Roblox Developing Utilities", programVersion)
print(" ")
print('''Please choose one of the available options by 
typing the number of the option and pressing [Enter]''')
print(" ")
print('''Options List:
1 - Gamepass 'Creator Earnings' Calculator
2 - Offset to Scale GUI Elements converter
 
Note: Type a capital 'D' after the number (no spaces)
like this: '1D' To see the Description of that utility.''')

utility = input("Select: ")

if utility == "1":
    print("You chose option '1'.")
    print(" ")
    print("Welcome to the Gamepass 'Creator Earnings' Calculator.")
    value = int(input("Please introduce the number you want to calculate: "))
    output = value * 0.70
    print(" ")
    print("You typed the number '", value, "'")
    fixedOutput = int(output)
    print(value, "- 30% =", fixedOutput)
    input("Press [Enter] to close ")

elif utility == "1D":
    print('''Description for "Gamepass 'Creator Earnings' Calculator"
    
This utility will help you to know how much robux you will actually earn from a gamepass.
Roblox takes 30% of the robux, and this will help you calculate it. Just type the cost of the pass,
and you will get the amount of robux you are going to get. Easy!''')
    print(" ")
    input("Press [Enter] to close ")

elif utility == "2":
    print("You chose option '2'.")
    print(" ")
    print("Welcome to the Offset to Scale GUI Elements converter.")
    screenWidth = int(input("Please, introduce the Width of the screen: "))
    screenHeight = int(input("Please, introduce the Height of the screen: "))
    offsetX = int(input("Please, introduce the 'X' offset of the element: "))
    offsetY = int(input("Please, introduce the 'Y' offset of the element: "))

    print("Your Roblox Studio screen resolution is", screenWidth, "X", screenHeight)
    print("The offset of the GUI Element is [ X", offsetX, "| Y", offsetY, "]")

    scaleX = offsetX / screenWidth
    scaleY = offsetY / screenHeight

    print(" ")
    print("The scales are [ X", scaleX, "| Y", scaleY, "]")
    print(" ")
    input("Press [Enter] to close ")