first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))
largest = first_number
text = 'The 1st Number is the greatest among three'

if second_number > first_number:
    if second_number > third_number:
        largest = second_number
        text = 'The 2nd Number is the greatest among three'
    else:
        largest = third_number
        text = 'The 3rd Number is the greatest among three'
elif third_number > first_number:
    if third_number > second_number:
        largest = third_number
        text = 'The 3rd Number is the greatest among three'
    else:
        largest = second_number
        text = 'The 2nd Number is the greatest among three'
print(f"1st Number = {first_number},        2nd Number = {second_number},        3rd Number = {third_number}")
print(text)