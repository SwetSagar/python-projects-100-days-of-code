"""
Calculating bill per person

"""


print("Welcome to this tip calculator! \n") # greetings

bill = float(input("Please enter the total bill :")) # enter the bill

persons_dining = int(input("Enter the total number of person who dined :")) # how many people ate together

tip = int(input("Enter the tip in percentatge, 10, 15, 20 etc. : ")) # tip willing to be paid

total_bill = bill + (bill * tip)/100 # calculating total bill including tip

per_person_charge = total_bill/ persons_dining # per person crude calculation

final_amount = round(per_person_charge, 2) 

print(f"The total bill per person is {final_amount}") # final display