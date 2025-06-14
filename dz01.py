from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - input_date
        return delta.days
    except ValueError:
        print ("Please enter correct date. Use YYYY-mm-dd")
    
print(get_days_from_today("2025-06-20"))  
# виводить  -6

print(get_days_from_today("25-06-20"))   
# виводить Please enter correct date. Use YYYY-mm-dd