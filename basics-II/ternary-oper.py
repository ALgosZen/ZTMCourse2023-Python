"""  Ternary operators evaluate something based on a condition being true or false """


try:
    a = int(input('Enter Integer value: '))
    b = int(input('Enter Integer value: '))
    min = a if a < b else b
    print('minimum value is : ', min)
except ValueError:
    print('Enter input integer only')

# second example

data = [2,4,6,7,3,2,1,5,7,9,8]

for num in data :
    # use ternary operator to determine even or odd 
    result = 'even' if num % 2 == 0 else 'odd'
    print(f'The number {num} is {result}')

# 3rd sample
""" modulus sets a modulus for the operation, effectively determining how many names should be in each row

:-^15 means Output at least 15 characters, even if the string is shorter than 15 characters.
Center align the string.
Fill any space on the right or left of the string with the hyphen character (-).

 """    
def split_names_into_rows(name_list, modulus=3):
    for index, name in enumerate(name_list, start=1):
        print(f"{name:-^15} ", end="")
        if index % modulus == 0:
            print()
    print()

namelist = ["Picard", "Riker", "Troi", "Crusher", "Worf", "Data", "La Forge"]

split_names_into_rows(namelist)

