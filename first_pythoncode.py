#Birthday Calculator 

months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
current_month = 9
birth_month = input("Which month were you born? Write the name of the month like January " )
if birth_month.lower() in months: 
    month_number= months.index(birth_month.lower()) +1
    
    if month_number == current_month: 
        birthday_in_months = 0 
    elif month_number > current_month:
        birthday_in_months = month_number - current_month
    else:
        (birthday_in_months) = 12- (current_month - month_number)

    if birthday_in_months == 0: 
        print("your Birthday is this Month!")
    else:
        print("your birtday is in " + str(birthday_in_months) + " months")
    
else:
    print("Your month is spelled wrongly")