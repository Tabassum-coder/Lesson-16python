#Function to calculate the bill

def total_calc(amount,tip):
    total=amount*(1+0.01*tip)
    total=round(total,2)
    
    print("Total bill to be paid is $",total)

amount=int(input("ENter the amount "))
tip=int(input("enter the tip"))
total_calc(amount,tip)