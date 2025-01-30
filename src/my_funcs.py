
# returns true of false if age is allowed to drive
# Work together
# Use code coverage to get suggestions on with code path to test
def allowed_to_drive(age):
    if age < 16:
        return False
    else:
        return True

# returns the largest value in a list
def get_largest_value_in_list(l):
    largest_value = None

    for e in l:
        if largest_value is None:
            largest_value = e
        elif e > largest_value:
            largest_value = e

        # largest_value = get_largest(largest_value, e)
    
    return largest_value

# def get_largest(a,b):
#     if a == None:
#         return b
#     elif b == None:
#         return a
#     elif a < b:
#         return b
#     else:
#         return a