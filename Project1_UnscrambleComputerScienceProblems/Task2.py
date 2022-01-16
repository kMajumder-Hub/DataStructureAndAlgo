"""
Read file into texts and calls.
It's ok if you don't understand how to read files
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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
if __name__ == '__main__':
    numbers = set()
    for call in calls:
        numbers.add(call[0])
        numbers.add(call[1])
    
    number_dict = dict.fromkeys(numbers, 0)
    
    for number in numbers:
        for i in range(0,len(calls)):
            if number == calls[i][0] or number == calls[i][1]:
                number_dict[number] = number_dict.get(number) + float(calls[i][3])

    number = None
    duration = 0
    for j in number_dict:
        if number_dict[j]>duration:
            number = j
            duration = number_dict[j]

    print(f'{number} spent the longest time, {duration} seconds, on the phone during September 2016.')