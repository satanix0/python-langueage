print("Welcome to bill calculator")
total =int(input("Enter Your total : "))
tip=int(input("How much tip would you like to add : "))
split = int(input("Number of people splitting the bill : "))
amt=(total+(total*(tip/100)))/split
print(f"Each person will pay ${round(amt)}")