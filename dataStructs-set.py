#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.

my_set = {1,2,4,5,6,7,8}
fruit_set =  {"apple", "banana", "cherry"}

##### built-in methods ######

# add()	Adds an element to the set , duplicate is ignored
my_set.add(9)
print(my_set)

# clear()	Removes all the elements from the set

# copy()	Returns a copy of the set
new_fruit_set = fruit_set.copy()

print(new_fruit_set)

# difference()	Returns a set containing the difference between two or more sets
new_fruit_set.add("grapes")
print(new_fruit_set)

added_fruit = new_fruit_set.difference(fruit_set)
print(added_fruit)


# difference_update()	Removes the items exists in both sets and lists only diff from first.
x = {"apple", "banana", "chewy"}
y = {"apple", "microsoft", "chewy"}
x.difference_update(y) 
print(x)

# discard()	Remove the specified item
x.remove("banana") # keyError if not exists
print(x)
# intersection()	Returns a set, that is the intersection of two or more sets


# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not

# issubset()	Returns whether another set contains this set or not
print(fruit_set.issubset(new_fruit_set))

# issuperset()	Returns whether this set contains another set or not
print(fruit_set.issuperset(new_fruit_set))

# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another


# union()	Return a set containing the union of sets
print(fruit_set.union(new_fruit_set))


# update()	Update the set with another set, or any other iterable

