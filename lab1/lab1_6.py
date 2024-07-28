
num = int(input("Enter a four-digit number: "))
sum= 0
rev = 0
temp = num

#checking whether num is 4 digit
if 1000 <= num <= 9999:
   
    while num > 0:
        digit = num % 10
        sum += digit
        rev = rev * 10 + digit
        num //= 10
    print(f"Sum of digits: {sum}")
    print(f"Reverse: {rev}")
else:
    print("Please enter a valid four-digit number.")


