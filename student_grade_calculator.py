
# Student Grade Calculator

name = input("Enter student name: ")

sub1 = int(input("Enter marks of Subject 1: "))
sub2 = int(input("Enter marks of Subject 2: "))
sub3 = int(input("Enter marks of Subject 3: "))

total = sub1 + sub2 + sub3 
average = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")   
elif average >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")     
