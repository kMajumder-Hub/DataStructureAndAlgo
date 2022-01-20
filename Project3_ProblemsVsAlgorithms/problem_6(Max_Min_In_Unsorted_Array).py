import random


def get_min_max(numbers):

    if(len(numbers) == 0):
        return None

    max_number = numbers[0]
    min_number = numbers[0]

    for number in numbers:

        if number > max_number:
            max_number = number

        if number < min_number:
            min_number = number
    return (min_number, max_number)


# Example Test Case of Ten Integers
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


# Test Case 1
l = [i for i in range(0, 9)]  # a list containing 0 - 9
random.shuffle(l)
print(get_min_max(l))
# should print(0,8)

# Test Case 2
l = [i for i in range(-30, 10)]  # a list containing -12 - 24
random.shuffle(l)
print(get_min_max(l))
# should print (-30,9)

# Test Case 3(Edge Case)
print('Edge Cases:')
# Case 1
l = [i for i in range(500, 501)]
random.shuffle(l)
print(get_min_max(l))
# shoukd print (500,500)

# Test Case 4(Edge Case)
l = []  # an empty list
print(get_min_max(l))
# should print None