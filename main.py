print("Welcome to the Python pizza deliveries !")

#users required questions
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")


#code logic of the challenge

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 10
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

#print the final bill
print(f"Your final bill is ${bill}")