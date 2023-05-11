import csv

# list of phone numbers
phone_numbers = [
'08037489900',
'07037489960',
'08037489907',
'08027489900' ,
'08037489988',
'09037489900',
'09030889900',
'09037489450',
'09023459900',
'08137489900',
'08137489934',
'08134489900',
'08137489910',
'08137487829', 
'08126487829',
'08137487771',
'08137487821',
'08034487829',
'08021487479',
]

# write phone numbers to CSV file
with open('phone_numbers.csv', mode='w', newline ='') as file:
    writer = csv.writer(file)
    writer.writerow(['Phone Numbers'])
    for number in phone_numbers:
        writer.writerow([number])

# read phone numbers from CSV file
with open('phone_numbers.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])