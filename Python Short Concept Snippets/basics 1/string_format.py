s = 'My name is {name} and I am {field} graduate'

s1 = s.format(name="Nipun", field="It")
print(s1)

s2 = s.format_map({'name': 'Dhruval', 'field': 'IT'})
print(s2)

s3 = 'Name is %s & Age is %d' % ("Nipun", 21)
print(s3)

s4 = "Isn't that joke so funny?! %r"
ans = False
print(s4 % ans)

#---------------

formatter = "%r %r"
print(formatter % (1,2))


# -------------------

d = {'name':'Naruto', 'age':20}
# AMAZING NOTE ->
# note here we are not using 'name' & 'age' inside {} still it works beauty of string formatting
s = "My name is {0[name]} and age is {0[age]}".format(d)
print(s)

# padding
print("{:02}".format(1)) # 01

# comma seperated value for large number
print("{:,}".format(1_000_000))  # 1,000,000

# Comma seperated & upto 2 decimal places :
print("{:,.2f}".format(1_000_000))  # 1,000,000.00


# Formatting a DATE :-------------------------

import datetime

date = datetime.datetime(2021, 10, 20, 2, 30)
f1 = "{:%B %d, %Y}".format(date) # Month day, year
print(f1) # October 20, 2021

s2 = "{0:%B %d, %Y} fell on {0:%A}, & day was {0:%j} of same year".format(date)
print(s2)  # October 20, 2021 fell on Wednesday, & day was 293 of same year
