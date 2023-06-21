def weekday_name(day_of_week):
    weekDays = [
        "Sunday",
        "Monday",
        "Tuesday",
        "wednesday",
        "Thursday",
        "friday",
        "Saturday",
    ]
    if day_of_week >= 1 and day_of_week <= 7:
        return weekDays[day_of_week - 1]
    else:
        return

    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
