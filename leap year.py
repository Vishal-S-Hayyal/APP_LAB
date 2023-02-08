print ("leap years between  2000,2025 are")
for year in range(2001, 2025):
  if  (0 == year % 4) and (0 != year % 100) or (0== year %400) :
    print (year)
