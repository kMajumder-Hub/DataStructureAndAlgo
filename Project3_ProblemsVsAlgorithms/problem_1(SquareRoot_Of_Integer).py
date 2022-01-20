def sqrt(number=None):

    if number is None:
        return None
    if number < 0:
        return None
    if number == 0 or number == 1:
        return number

    start = 0
    end = number

    while(start < end):
        mid = (start+end)//2
        mid_pow = mid*mid

        if mid_pow == number:
            return mid
        elif mid_pow < number:
            start = mid+1
            result = mid
        else:
            end = mid
    return result



# Test Case 1
print(sqrt(4))
# should print 2

# Test Case 2
print(sqrt(16))
# should print 4

# Test Case 3
print(sqrt(99856))
# should print 316

# Test Case 4(Edge Case)
print(sqrt())
# should print None

# Test Case 5(Edge Case)
print(sqrt(-1))
# should print None