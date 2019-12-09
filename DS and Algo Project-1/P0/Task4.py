"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

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

def telemarket_checker(calls, texts):
    send_text = set()
    recieve_text = set()
    recieve_call = set()
    for i in calls:
        if i[1] not in recieve_call:
            recieve_call.add(i[1])
    for i in texts:
        if i[0] not in send_text:
            send_text.add(i[0])
        if i[1] not in recieve_text:
            recieve_text.add(i[1])
    telemarketer = []
    for i in calls:
        if i[0] not in send_text and i[0] not in recieve_text and i[0] not in recieve_call:
            telemarketer.append(i[0])        
    return sorted(set(telemarketer))

tele = telemarket_checker(calls, texts)
print("These numbers could be telemarketers: ")
for i in tele:
    print(i)
