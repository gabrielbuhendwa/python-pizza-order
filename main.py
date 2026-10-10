print("Welcome to the Python pizza deliveries !")

#users required questions
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


#code logic of the challenge

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 10
else:
    bill += 25
