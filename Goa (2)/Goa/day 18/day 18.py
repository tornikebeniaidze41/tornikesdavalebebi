# name = "Giorgi"
# even_indexes_string = ''
#         #  0 1 2 3 4 5
# for i in range(0, len(name)):
#     if i % 2 == 0:
#         even_indexes_string = even_indexes_string + name[i]

# print(even_indexes_string)

#პირველ რიგში ვქმნით ცვლადს სახელად name რომელიც შეიცავს string-ს, "Giorgi"
#ასევე ვქმნით ცვლადს სახელად even_indexes_string რომელიც შეიცავს ცარიელ string-ს
#შემდეგ for loop-ის გამოყენებით, ათვლა იწყება 0-დან და მთავრდება name ცვლადის სიგრძის აღმნიშვნელ რიცხვთან
#ამ for loop-ის გამოყენებით, ჩვენ ასევე ვაარსებთ ცვლადს სახელად i, და კოდში შემდეგ %-ის გამოყენებით ვარკვევთ i ლუწია თუ არა
#თუ ლუწია, მაშინ name ცვლადის i ინდექსზე მყოფ ელემენტს ვუმატებთ ცვლად even_indexes_string-ს
#ბოლოში ვბეჭდავთ ცვლად even_indexes_string-ს, ამ შემთხვევაში გამოგვდის Gog


#1
place = 'saqartvelo'
odd_indexes_string = ''

for i in range(0, len(place)):
    if i%2!=0:
        odd_indexes_string += place[i]
print(odd_indexes_string)

#2
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
multiples_of_five = []

for i in range(len(list)):
    if list[i]%5 == 0:
        multiples_of_five.append(list[i])
print(multiples_of_five)

#3
name = 'tornike'
vowels = ['a','e','i','o','u','y']
vowels_in_name = ''
for i in range(len(name)):
    if name[i] in vowels:
        vowels_in_name += name[i]
print(vowels_in_name)

#4
name = 'giorgi'
vowels = ['a','e','i','o','u','y']
consonants_in_name = ''
for i in range(len(name)):
    if name[i] in vowels:
        name = name
    else:
        consonants_in_name += name[i]
print(consonants_in_name)

#5
word = 'pneumonoultramicroscopicsilicovolcanoconiosis'
repeated_letters = ''
for i in range(len(word)):
    x = 0
    for j in range(len(word)):
        if word[i] == word[j] and i != j:
            x +=1
    if x>0:
        if word[i] in repeated_letters:
            word = word
        else:
            repeated_letters += word[i]
print(repeated_letters)
        

#შემოკლებული მინიჭების ოპერატორები:

#1
num = 17
num+=15
num*=120
num/=12
num%=100
print(num)

#2
num = 11
num+=180
num*=12
num/=13
num%=99
print(num)

#3
num = 1701
num+=12
num*=129
num/=13
num%=101
print(num)