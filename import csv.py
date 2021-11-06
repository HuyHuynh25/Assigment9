########################################################################
 ##
 ## CS 101 Lab
 ## Program 9
 ## Name: Huynh Gia Huy-Jim Huynh
 ## Email: hghydv@umsystem.edu
 ##
 ## PROBLEM : Create write a program to read in a datafile containing crime information for 2019
 ## You can open the csv files in excel to view it as rows and columns, but make sure you don’t save any changes.
 ## You can also open the file in a text editor to see how it is actually stored character by character.
 ## ALGORITHM :
 ##      Step 1:  Start
 ##      Step 2:  Import csv
 ##      Step 3:  Define function month_from_number(month)
 ##      Step 4:  Define function read_in_file(file_name)
 ##      Step 5:  Define function create_reported_date_dict(data)
 ##      Step 6:  Define function create_reported_month_dict(data)
 ##      Step 7:  Define function create_offense_dict(data)
 ##      Step 10: Define function create_offense_by_zip_dict(data) 
 ##      Step 11: Make a loop if it's True
 ##      Step 12: Declare input to ask crime data file
 ##      Step 13: Call create_reported_month_dict(data) and create_offense_dict(data) to create highest 
 ##               month and offense
 ##      Step 14: Make another loop if it's True
 ##      Step 15: Call create_offense_by_zip_dict(data)
 ##      Step 16: Declare input for enter an offense
 ##      Step 17: Make an if function user_input in offense_by_zip 
 ##      Step 18: End
 ##ERROR HANDLING
 ##      N/A
 ##
 ## OTHER COMMENTS:
 ##      Any special comments
 ##
 ########################################################################
import csv
def month_from_number(month):
    list_of_month = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',
                     10:'October',11:'November',12:'December'}
    if not 0 < month < 13:
        raise ValueError("Month must be 1-12")
    else:
        return list_of_month[month]
def read_in_file(file_name):
    file_data = []
    with open(file_name, encoding='utf-8') as file:
        file_csv = csv.reader(file)
        for line in file_csv:
            file_data.append(line)
    return file_data
def create_reported_date_dict(data):
    date_dict = {}
    for row in data[1:]:
        key = row[1]
        date_dict[key] = date_dict.get(key, 0) + 1
    return date_dict
def create_reported_month_dict(data):
    month_dict = {}
    for row in data[1:]:
        if int(row[1][0:2]) in month_dict:
            month_dict[int(row[1][0:2])] += 1
        else:
            month_dict[int(row[1][0:2])] = 1
    return month_dict
def create_offense_dict(data):
    offense_dict = {}
    for row in data[1:]:
        if str(row[7].split(' – ')[0]) in offense_dict:
            offense_dict[str(row[7].split(' – ')[0])] += 1
        else:
            offense_dict[(row[7].split(' – ')[0])] = 1
    return (offense_dict)
def create_offense_by_zip_dict(data):
    offense_by_zip_dict = {}
    for row in data[1:]:
        if str(row[7].split(' – ')[0]) in offense_by_zip_dict:
            if row[13] in offense_by_zip_dict[str(row[7].split(' – ')[0])]:
                offense_by_zip_dict[str(row[7].split(' – ')[0])][row[13]] += 1
            else:
                offense_by_zip_dict[str(row[7].split(' – ')[0])][row[13]] = 1
        else:
            offense_by_zip_dict[str(row[7].split(' – ')[0])] = {row[13]: 1}
    return (offense_by_zip_dict)
if __name__ == "__main__" :
    while True:
        user_file = input('Enter the name of the crime data file: ==>')
        try:
            data = read_in_file(user_file)
            break
        except FileNotFoundError:
            print('Could not find the file {} not found'.format(user_file))
    month = create_reported_month_dict(data)
    crime_month = dict(sorted(month.items(), key=lambda x: x[1], reverse=True))
    offense = create_offense_dict(data)
    crime_offense = dict(sorted(offense.items(), key=lambda x: x[1], reverse=True))
    print()
    print('The month with the highest # of crimes is {} with {} offenses'.format(
        month_from_number(list(crime_month.keys())[0]), list(crime_month.values())[0]))
    print('The offense with the highest # of offenses is {} (Non-Aggravated) with {} offenses'.format(list(crime_offense.keys())[0],
                                                                                     list(crime_offense.values())[0]))

    while True:
        offense_by_zip = create_offense_by_zip_dict(data)
        print()
        user_input = input('Enter an offense: ')
        if user_input in offense_by_zip:
            print()
            print('{} offense by Zip Code'.format(user_input))
            print('{:<5}{:>52}'.format('Zip Code', '# Offenses'))
            print('=' * 60)
            for key in offense_by_zip[user_input]:
                print('{:<5}{:>55}'.format(key, offense_by_zip[user_input][key]))
            break
        else:
            print('Not a valid offense found, please try again')

