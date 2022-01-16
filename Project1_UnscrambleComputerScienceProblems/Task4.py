"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
texts = []
calls = []
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
if __name__ == '__main__':
    numbers = set()
    for call in calls:
        numbers.add(call[0])

    marketing_list = []
    for number in numbers:
        flag = True
        for call in calls:
            if number == call[1]:
                flag = False
                break
        if flag == True:
            for text in texts:
                if number == text[0] or number == text[1]:
                    flag = False
                    break
        if flag == True:
            marketing_list.append(number)

    marketing_list.sort()
    print(f'These numbers could be telemarketers: {marketing_list}')