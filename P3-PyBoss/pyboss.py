import os
import csv

# Set path for source file
ee_csv = os.path.join("employee_data.csv")

import datetime

# store data in list
empl_id = []
fname = []
lname = []
dob = []
ssn_last4 = []
state_abr = []
ssn = ' '
yyyyddmm = ' '

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
# Open the CSV
with open(ee_csv) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    next(reader) #skip header row
    
    # read through the employee csv file and reformat records
    for row in reader:
        
        empl_id.append(row[0])
        
        #split name into fname, lname
        fname.append(row[1].split()[0])
        lname.append(row[1].split()[1])
        
        #reformat date from yyyy/mm/dd to mm/dd/yyyy
        yyyyddmm = row[2]
        dob.append(datetime.datetime.strptime(yyyyddmm,'%Y-%m-%d').strftime('%m/%d/%Y'))       
        
        #hide first 5 digits of ssn
        ssn = row[3]
        ssn_last4.append("***-**-" + str(ssn[7:11]))
        
        #abbreviate state
        state_abr.append(us_state_abbrev.get(row[4])) 
    
#zip lists together
zipped_data = zip(empl_id, fname, lname, dob, ssn_last4, state_abr) 
#print(tuple(zipped_data))

# Set variable for output file
output_file = os.path.join("new_employee_data.csv")

# Open the output new eemployee csv file 
with open(output_file, "w",newline='') as datafile:
        writer = csv.writer(datafile, delimiter=',')
            
        # Write the header row and zipped rows
        writer.writerow(["Empl ID","First Name","Last Name","DOB","SSN","State"])
        writer.writerows(zipped_data)
        print("Woo Hoo!  Your new employee file is ready to review.")