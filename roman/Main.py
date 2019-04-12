from datetime import datetime
from NumberToRoman import numbertoRoman
from ValidateDate import validate

# Get a value from User
providedDate = input("Please provide a date to be convered into a Roman Numeral: ")
validate(providedDate)

# Get Year | Month | Day
year = datetime.strptime(providedDate , '%m/%d/%Y').year
month = datetime.strptime(providedDate , '%m/%d/%Y').month
day = datetime.strptime(providedDate , '%m/%d/%Y').day

#Convert to Roman Numeral 
RomanYear = numbertoRoman(year)
RomanMonth = numbertoRoman(month)
RomanDay = numbertoRoman(day)

#Put back together and print 
RomanDate = RomanMonth + "/" + RomanDay + "/" +  RomanYear
print (RomanDate)

