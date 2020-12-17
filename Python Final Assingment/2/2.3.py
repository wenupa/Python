bill = int(input("Enter the bill amount : "))
if bill > 5000:
    disc = bill * 10/100
else:
    disc = bill * 5/100
print("Your Discount Price is :",disc)
