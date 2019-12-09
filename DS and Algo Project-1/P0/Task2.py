"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
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

def longest_usage(list):
    count = {}
    for i in list:
        if i[0] in count:
            count[i[0]] += int(i[3])
        else:
            count[i[0]] = int(i[3])
        if i[1] in count:
            count[i[1]] += int(i[3])
        else:
            count[i[1]] = int(i[3])
    max_usage = 0
    max_usage_no = ''
    for i in count:
        if max_usage < count[i]:
            max_usage = count[i]
            max_usage_no = i
    if max_usage == 0:
        return None
    else:
        return max_usage, max_usage_no

time, number = longest_usage(calls)
print(number + ' spent the longest time, {} seconds, on the phone during Sptember 2016.'.format(time))

