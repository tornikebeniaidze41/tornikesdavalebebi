# name = "beno"
# Name=name.upper()
# def NAme (string):
#     return string[::-1]
# NAme=NAme(Name)
# print(NAme)




# def classify_strings(strings):
#     odd = []
#     even = []
    
#     for string in strings:
#         if len(string) % 2 == 0:
#             even.append(string.upper())
#         else:
#             odd.append(string.upper())
    
#     return odd, even



# def transform_strings(strings):
#     result = []
#     for string in strings:
#         if len(string) % 2 == 0:
#             result.append(string.upper())
#         else:
#             result.append(string[0].upper() + string[1:].lower())
#     return result



# def transform_case(strings):
#     result_list = []
#     for string in strings:
#         if string.isupper():
#             result_list.append(string.lower())
#         elif string.islower():
#             result_list.append(string.upper())
#         else:
#             result_list.append(string)
#     return result_list




# def transform_string(string):
#     index = string.find(" ")
#     if index % 2 == 0:
#         return string.upper()
#     else:  # Odd index
#         return string.capitalize()





