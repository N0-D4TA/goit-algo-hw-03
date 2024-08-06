from datetime import datetime


def get_days_from_today(date: str) -> int:
    try:
       
       # Parsing string to datetime object
       from_today = datetime.strptime(date, '%Y-%m-%d') 
    except ValueError:

        # Wrong input exception handling
        return 'Wrong input, use actual date in YYYY-MM-DD.' 
    
    today = datetime.today()
    
    # Calculating raw number of days
    days_difference = (from_today - today).days 
    return days_difference