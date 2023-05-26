is_old = False
is_licensed = False 

if is_old and is_licensed:
    print('you are old enough to drive and have license!')
elif not is_old:
    print('you are not old enough to drive')
elif not is_licensed:
    print('you need license to drive')
print('outside conditions..') # executes default after condition

# nunber 0 and empty string evaluate to false!! wierd . here is more..
""" All values are considered "truthy" except for the following, which are "falsy": """
""" https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false
 """
# None
# False
# Numbers that are numerically equal to zero, including:
# 0
# 0.0
# 0j
# decimal.Decimal(0)
# fraction.Fraction(0, 1)
# Empty sequences and collections, including:
# [] - an empty list
# {} - an empty dict
# () - an empty tuple
# set() - an empty set
# '' - an empty str
# b'' - an empty bytes
# bytearray(b'') - an empty bytearray
# memoryview(b'') - an empty memoryview
# an empty range, like range(0)
# objects for which
# obj.__bool__() returns False
# obj.__len__() returns 0, given that obj.__bool__ is undefined

# print(bool([]))
# print(bool(0))
# print(bool(''))
# print(bool({}))
# print(bool(()))
print(bool(set()))

# interesting Truthy and Falsy checks. 
my_list = []
if(my_list):
    print('Not empty')
else:
    print('Empty')

# python determines the truthiness by applying bool() to the type 

