numbers = [1,2,3,4,5,6,7,8,9,10]

odd_sum = 0
odd_multiple = 1

for num in numbers:
    if num % 2 != 0:
        odd_sum = odd_sum + num
        odd_multiple = odd_multiple * num

print("Odd numbers sum", odd_sum)
print("Odd numbers multiple", odd_multiple)