#Anthony Raynor
#10/17/2024
#P2HW2
#Calculate the average grades

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))
grades = [module1, module2, module3, module4, module5, module6]
sum_of_grades = module1 + module2 + module3 + module4 + module5 + module6
print()
print('-----------Results-----------')
print(f"{'Lowest Grade':<20}{min(grades)}")
print(f"{'Highest Grade':<20}{max(grades)}")
print(f"{'Sum of Grades:':<20}{sum_of_grades:,.2f}")
average = sum(grades)/len(grades)
print(f"{'Average:':<20}{average:,.2f}")
print("-" * 40)
