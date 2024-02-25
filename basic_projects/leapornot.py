'''Leap year or not'''

year_to_check = int(input("Enter year to check if leap or not : "))

if year_to_check % 4 == 0: # Nested if to check further condition if divisible by 4 and 100 then not leap
    if year_to_check % 400 == 0:
        print ("It is a leap year")
    elif year_to_check % 100 == 0:
        print("It is not a leap year")
    else :
        print("Yes it is a leap year")
else : # for all other cases where not divisible by 4
    print("It is not a leap year!")