#Anthony Raynor
#10/29/24
#P3HW2
#Calculates how much money user makes an hour
'''
Input: Get employee's name from user-string(name)
Input: Get hours worked from user - int (hours)
Input: Get pay rate from user- float (pay_rate)

output: print dotted line and employee name

if hour is greater than  40 (employee has OT)
    variable for house worked already exist(dont re-create)
    total hours worked is the variable hours(optional)
    (dont have to create pay rate, it already exists)
    create a variable(OT) that holds the OT hours (hours - 40)
    create a variable for the OT_pay_rate (pay_rate * 1.5)
    calculate pay for OT hours (OT * OT_pay_rate)
    calculate regular pay (pay_rate * 40)
    calculate gross pay (pay for OT + regular pay)
else (NO OT - hours has to be 40 or less)
    create a variable (OT) that holds only the OT hours WHICH IS ZERO
    calculate pay for OT hours Which is zero
    calculate regular pay (pay_rate * hours)
    calculate gross pay (same as regular pay)

Display the line of strings with width specifiers
print(f"{'Hours Worked':<20}{'Pay Rate':<20}")
print(f"{hours:<20}${pay_rate:<20.2f}")



'''
name = input("Enter employees name: ")
hours = int(input("Enter number of hours work: "))
pay_rate = float(input("Enter employees pay rate: "))
print("-" * 35)
print(f"Employee name: {name}")
print()

if hours > 40:
    ot = hours - 40
    ot_pay_rate = pay_rate * 1.5
    ot_pay = ot * ot_pay_rate
    regular_pay = pay_rate * 40
    gross_pay = ot_pay + regular_pay
else:
    ot = 0
    ot_pay = 0
    regular_pay = pay_rate * hours
    gross_pay = regular_pay

print(f"{'Hours Worked':<20}{'Pay rate':<20}{'Overtime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
print("-" * 110)
print(f"{hours:<20}${pay_rate:<20.2f}{ot:<20}${ot_pay:<20.2f}${regular_pay:<20.2f}${gross_pay:<20.2f}")        




    



