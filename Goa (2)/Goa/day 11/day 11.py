#1

for i in range(1, 51):
    if i%5==0:
        print(i)
        
#2

for i in range(2,21):
    if i%2==0:
        print(i)
        
#3

x = 1
for i in range(5,11):
    x *= i
print(x)

#4

num = int(input('Please enter a number: '))
x = 1

for i in range(1, num+1):
    x*=i
print(x)

#5

num = int(input('Please enter a number:'))

if num%2==0:
    num/=2
else:
    num*=3
    num+=1
print(num)



#While loop:

#1

num = 10

while num > 0:
    print(num)
    num-=1

#2

name = input('Please enter your name: ')
while name.lower() != 'quit':
    name = input('Please enter your name: ')


#3

num = 10

while num <= 20:
    if num%2==0:
        print(num)
    num+=1
    
#4

num = int(input('Please enter a number: '))

while num <= 0:
    num = int(input('Please enter a number: '))
print(num)

#5

num = 1

while num <= 10:
    print(num*num)
    num +=1