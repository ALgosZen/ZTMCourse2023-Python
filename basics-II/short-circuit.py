#short circuiting using OR

is_friend = True 
is_user = True 
# since first evaluation returns True(or false) , python ignores the second evaluation.
if is_friend or is_user:
    print('best friends forever')
