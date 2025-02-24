rent = int(input("Enter the Room/Flat rent : "))
electricity = int(input("Enter electricity bill : "))
food = int(input("Enter amount spent on food ordering : "))
person = int(input("Enter the number of person living in the room : "))

totalExpence = rent + electricity + food 
print(f"Each person has to pay {totalExpence//person}")