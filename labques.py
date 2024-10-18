S1 = "Maha Bharat"


S2 = S1.swapcase()
print(S2)


S3 = S1.split()[1]
print(S3)


S4 = S3 * 3
print(S4)


S5 = S1.replace("Maha", "Mera")
print(S5)


S6 = S5 + " Mahan"
print(S6)

print("-------=====================-----------------===============")




S = "Ba Ba Black Sheep"


length_of_S = len(S)
print(f"Length of the string: {length_of_S}")

first_occurrence_e = S.find('e')
print(f"First occurrence of 'e': {first_occurrence_e}")

total_occurrences_a = S.count('a')
print(f"Total number of occurrences of 'a': {total_occurrences_a}")


modified_string = S.replace("Ba", "Ta", 2) 
print(f"Modified string: {modified_string}")



print("-------=====================-----------------===============")



string = input("Enter a string: ")


normalized_string = string.replace(" ", "").lower()


if normalized_string == normalized_string[::-1]:
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')



print("-------=====================-----------------===============")








import math

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))


if a == 0:
    print("The value of 'a' must not be zero for a quadratic equation.")
else:
   
    discriminant = b**2 - 4*a*c


    if discriminant > 0:
    
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"The roots are real and distinct: {root1} and {root2}")
    elif discriminant == 0:
       
        root = -b / (2*a)
        print(f"The roots are real and equal: {root}")
    else:
      
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        print(f"The roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")



print("-------=====================-----------------===============")


        
name = input("Enter the student's name: ")
roll_number = input("Enter the roll number: ")
marks = int(input("Enter the marks secured in Mathematics out of 100: "))

if marks >= 90:
    grade_point = 10
    remark = "OUTSTANDING"
elif 80 <= marks < 90:
    grade_point = 9
    remark = "VERY GOOD"
elif 70 <= marks < 80:
    grade_point = 8
    remark = "GOOD"
elif 60 <= marks < 70:
    grade_point = 7
    remark = "AVERAGE"
elif 50 <= marks < 60:
    grade_point = 6
    remark = "PASS"
else:
    grade_point = 0
    remark = "FAIL"


print("\nStudent Details:")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Marks: {marks}")
print(f"Grade Point: {grade_point}")
print(f"Remark: {remark}")

